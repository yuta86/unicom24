from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from account.models import Profile, Request
from account.forms import UserForm, ProfileForm, UserFormForEdit, RequestForm

from django.db import transaction
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def home(request):
    return redirect(account_home)


# Декоратор login_required
# проверяет, прошел ли текущий пользователь аутентификацию.
# Если пользователь прошел аутентификацию, представление выполнится; Если пользователь не прошел
# аутентификацию, он будет перенаправлян на страницу входа '/account/sign-in/').

@login_required(login_url='/account/sign-in/')
def account_home(request):
    return redirect(account_orders)


@login_required(login_url='/account/sign-in/')
@transaction.atomic
def account_account(request):
    user_form = UserFormForEdit(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    if request.method == "POST":
        user_form = UserFormForEdit(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлён.')
        else:
            messages.error(request, 'Ошибка при обновлении профиля!')
    return render(request, 'account/account.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        # 'photo': request.user.profile.photo
    })


@login_required(login_url='/account/sign-in/')
def account_orders(request):
    orders = Request.objects.filter(profile=request.user.profile)
        # .order_by("-id")
    return render(request, 'account/orders.html', {
        'orders': orders
    })


@login_required(login_url='/account/sign-in/')
def account_add_orders(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.profile = request.user.profile
            order.save()
            return redirect(account_orders)

    return render(request, 'account/add_orders.html', {
        'form': form,

    })


@login_required(login_url='/account/sign-in/')
def account_edit_orders(request, order_id):
    form = RequestForm(instance=Request.objects.get(id=order_id))
    if request.method == 'POST':
        form = RequestForm(request.POST, request.FILES, instance=Request.objects.get(id=order_id))
        if form.is_valid():
            order = form.save()
            messages.success(request, 'Ваша заявка успешно обновлена.')
            return redirect(account_orders)
        else:
            messages.error(request, 'Ошибка при обновлении заявки!')
    return render(request, 'account/edit_orders.html', {
        'form': form,

    })


# authenticate() проверяет учетные данные пользователя и возвращает user объект в случае успеха;
# login() задает пользователя в текущей сессии.
def account_sign_up(request):
    user_form = UserForm()
    profile_form = ProfileForm()
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_profile = profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()

            login(request, authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            ))
            return redirect(account_home)
    return render(request, 'account/sign_up.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


#########################################################################################
from rest_framework import generics
from account.models import Profile, Offer, Partner
from account.serializers import UserSerializer, ProfileSerializer, OfferSerializer, PartnerSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response


class ProfileListView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileDatailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class OfferListView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class OfferDatailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer


class PartnerListView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class PartnerDatailView(generics.RetrieveAPIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer

