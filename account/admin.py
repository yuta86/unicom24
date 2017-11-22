from django.contrib import admin
from .models import Profile, Offer, Partner, Request
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.db import models
from django.forms import widgets


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo', 'sex', 'city', 'passport', 'phone', 'score',
                    'social_status', 'group']  # вывод указанных полей
    list_editable = ['date_of_birth', 'photo', 'sex', 'city', 'passport', 'phone', 'score',
                     'social_status', 'group']  # поля для редактирования в Админке
    list_filter = ['city', 'score', 'social_status', 'group']  # фильтр по столбцу
    search_fields = ['city', 'passport', 'phone', 'user']  # поиск по столбцам

    # list_display_links = ['city']  # ссылочные поля

    # ordering = ['user'] # сортировка
    # fields = ['city'] отображение полей
    # exclude = ['city'] неотображаемые поля
    # readonly_fields = ['city'] поля для чтения
    # fieldsets = [   # разделение формы на две и более частей
    #     (None,
    #      {'fields': ['user', 'date_of_birth', 'city', 'photo', 'phone'] }),
    #     ('Data information', {'fields': ['group','passport', 'score', 'sex', 'social_status'],
    #                           'classes': ['collapse']})
    # ]

    # переопределение виджета DateField
    # formfield_overrides = {
    #     models.DateField: {'widget': widgets.TextInput}
    # }


admin.site.register(Profile, ProfileAdmin)


class ProfileUser(UserAdmin):
    list_display = ['id', 'last_login', 'first_name', 'last_name', 'email', 'date_joined', 'username', 'is_staff',
                    'is_active']  # вывод указанных полей
    list_editable = ['last_login', 'first_name', 'last_name', 'email', 'date_joined', 'username', 'is_staff',
                     'is_active']  # поля для редактирования в Админке
    list_filter = ['date_joined', 'username', 'is_staff', 'is_active']  # фильтр по столбцу
    search_fields = ['first_name', 'last_name', 'email', ]  # поиск по столбцам


admin.site.unregister(User)
admin.site.register(User, ProfileUser)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image']  # вывод указанных полей
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']  # поиск по столбцам
    list_editable = ['slug', 'image']  # поля для редактирования в Админке
    # prepopulated_fields, чтобы указать поля, в которых значение автоматически задается с использованием значения других полей


admin.site.register(Partner, PartnerAdmin)


class OfferAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'partner', 'image', 'description', 'available', 'begin', 'end', 'min_score',
                    'max_score', 'created', 'updated']  # вывод указанных полей
    list_filter = ['partner', 'available', 'created', 'updated']  # фильтр по столбцу
    list_editable = ['begin', 'end', 'available', 'min_score', 'max_score']  # поля для редактирования в Админке
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'email']  # поиск по столбцам

    save_as = True  # для появления кнопки "Сохранить как"
    save_on_top = True  # дополнительные кнопки сверху


admin.site.register(Offer, OfferAdmin)


class RequestAdmin(admin.ModelAdmin):
    list_display = ['profile', 'offer', 'created', 'updated', 'type_status']  # вывод указанных полей
    list_filter = ['created', 'offer', 'type_status']  # фильтр по столбцу
    list_editable = ['type_status']  # поля для редактирования в Админке
    search_fields = ['created', 'offer', 'type_status']  # поиск по столбцам
    # raw_id_fields = ['offer'] создание доп. окна, как выбор из списка


admin.site.register(Request, RequestAdmin)
