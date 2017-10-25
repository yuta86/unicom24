from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

social_status_choices = (
    ('schoolboy', 'Школьник'),
    ('student', 'Студент'),
    ('working', 'Рабочий'),
    ('сivil_servant', 'Госслужащий'),
    ('businessman', 'Предприниматель'),
    ('unemployed', 'Безработный'),
    ('other', 'Другое'),
)

group_choices = (
    ('superuser', 'Суперпользователь'),
    ('partner', 'Партнёр'),
    ('bank', 'Кредитная организация'),
    ('user', 'Пользователь'),
)

sex_choices = (
    ('male', 'мужской'),
    ('female', 'женский'),
)

type_offer_choices = (
    ('potreb', 'Потребительский кредит'),
    ('ipoteka', 'Ипотека'),
    ('auto', 'Автокредит'),
    ('kmsb', 'Кредит М и С бизнеса'),
)


class Profile(models.Model):
    # вторичный ключ на таблицу User
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # related_name - задаёт имя модели для обратной связи  от связной модели. Если не хотите создавать обратную связь, то
    # related_name = '+'
    # blank = True: пустая строка допустима
    # Дата рождения
    date_of_birth = models.DateField(blank=True, null=True, default='2010-01-01', verbose_name='Дата рождения')
    # Населённый пункт
    city = models.CharField(max_length=30, blank=True, default='Москва', verbose_name="Населённый пункт")
    # Фото (Аватар)
    photo = models.ImageField(upload_to='users/', blank=False, verbose_name="Фото")

    # Номер телефона (Мобильный)
    phone = models.CharField(max_length=12, verbose_name="Телефон")  # +7 XXX XXX XXXX
    # Серия номер паспорта 1234 123456
    passport = models.CharField(max_length=10, verbose_name="Паспорт")
    # Скоринговый балл
    score = models.DecimalField(max_digits=10, default='10', decimal_places=2)  # скоринговый балл
    # пол

    sex = models.CharField(max_length=10, choices=sex_choices, default='male', verbose_name="пол")

    # социальный статус школьник студент работающий, бизнесмен и тд

    social_status = models.CharField(max_length=20, choices=social_status_choices, default='other',
                                     verbose_name="Социальный статус")

    group = models.CharField(max_length=20, choices=group_choices, default='user',
                             verbose_name="Группа пользователя")

    class Meta:
        ordering = ('user',)
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        # unique_together = ["phone", User.email ]

    def __str__(self):
        # return 'Profile for user {}'.format(self.user.username)
        return "%s - %s - %s" % (self.user.username, self.city, self.passport)


class Partner(models.Model):  # кредитная организация
    name = models.CharField(max_length=200, db_index=True, unique=True, verbose_name="Название партнёра")
    slug = models.CharField(max_length=200, db_index=True, unique=True)
    # Иконка партнёра.
    # 'offers/partner/%s' % (name)
    image = models.ImageField(upload_to='offers/partner/', blank=True, verbose_name="Изображение")

    class Meta:
        ordering = ('name',)
        verbose_name = 'Партнёр'
        verbose_name_plural = 'Партнёры'

    def __str__(self):
        return self.name


class Offer(models.Model):
    # Название предложения.
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название предложения")
    # Алиас предложения(его URL).
    slug = models.SlugField(max_length=200, db_index=True)
    # Партнёр
    partner = models.ForeignKey(Partner, related_name='partner', on_delete=models.CASCADE, verbose_name="Партнёр")
    # related_name - задаёт имя модели для обратной связи  от связной модели. Если не хотите создавать обратную связь, то
    # related_name = '+'

    # Изображение предложения.
    image = models.ImageField(upload_to='offers/', blank=True)
    # Описание
    description = models.TextField(blank=True, verbose_name="Описание")
    # Статус предложения
    available = models.BooleanField(default=True, verbose_name="Статус предложения")
    # минимальный скоринговый балл
    min_score = models.DecimalField(max_digits=10, default='0', decimal_places=2,
                                    verbose_name="минимальный скоринговый балл")  # скоринговый бал
    # максимальный скоринговый балл
    max_score = models.DecimalField(max_digits=10, default='10', decimal_places=2,
                                    verbose_name="максимальный скоринговый балл")  # скоринговый бал
    # Типы кредитов
    type_offer = models.CharField(max_length=20, choices=type_offer_choices, default='potreb',
                                  verbose_name="Тип предложения")
    # Начало ротации
    begin = models.DateTimeField(verbose_name="Начало ротации")
    # Окончание ротации
    end = models.DateTimeField(verbose_name="Окончание ротации")
    # Дата создания
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    # Дата обновления
    # В этом поле хранится время последнего обновления объекта
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлён")

    class Meta:
        ordering = ('name',)  # сортировка
        index_together = (('id', 'slug'),)
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # Конвенция для получения URL-адреса данного объекта
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class Request(models.Model):
    # вторичный ключ на таблицу Profile
    profile = models.ForeignKey(Profile, related_name='profile', on_delete=models.CASCADE, verbose_name="Клиент")
    # вторичный ключ на таблицу Offer
    offer = models.ForeignKey(Offer, related_name='offer', on_delete=models.CASCADE, verbose_name="Предложение")
    # Дата создания
    created = models.DateTimeField(auto_now_add=True, verbose_name="Создан")
    # Дата обновления
    # В этом поле хранится время последнего обновления объекта
    updated = models.DateTimeField(auto_now=True, verbose_name="Обновлён")
    # Типы запросов
    type_status_choices = (
        ('Новый', 'Новый'),
        ('Отправлено', 'Отправлено'),

    )
    type_status = models.CharField(max_length=20, choices=type_status_choices, default='Новый',
                                   verbose_name="Статус")

    def __str__(self):
        return "%s %s %s" % (self.type_status, self.profile_id, self.offer_id)

    class Meta:
        ordering = ('created',)  # сортировка
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
