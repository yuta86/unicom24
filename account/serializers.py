from django.contrib.auth.models import User
from rest_framework import serializers
from account.models import Offer, Profile, Partner, Request


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    def get_photo(self, profile):
        request = self.context.get('request')
        photo_url = profile.photo.url

        return request.build_absolute_uri(photo_url)
    class Meta:
        model = Profile
        fields = (
            'user', 'date_of_birth', 'city', 'photo', 'phone', 'passport', 'score', 'sex', 'social_status', 'group')


class RequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Request
        fields = ('id', 'offer', 'profile', 'created', 'updated')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = (
            'name', 'slug', 'partner', 'image', 'description', 'available', 'min_score', 'max_score', 'type_offer',
            'begin', 'end', 'created', 'updated')


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ('name', 'slug', 'image')
