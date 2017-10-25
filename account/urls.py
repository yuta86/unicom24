# from django.conf.urls import url
# from . import views
# from django.contrib.auth import views as auth_views
# from account import views
#
#
#
# urlpatterns = [
#     # url(r'^$', views.dashboard, name='dashboard'),
#     url(r'^$', views.home, name='home'),
#     # регистрация
#     url(r'^sign-up/$', views.sign_up, name='sign_up'),
#
#     # url(r'^edit/$', views.edit, name='edit'),
#     # вход
#     url(r'^sign-in/$', auth_views.login, {'template_name': 'account/sign_in.html'}, name='sign_in'),
#     # выход
#     url(r'^sign-out/$', auth_views.logout, {'next_page': '/'}, name='sign_out'),
#
#     # url(r'^account/$', views.unicom24_home, name='unicom24_home'),
#     #
#     url(r'^account/$', views.account, name='account'),
#
#     url(r'orders/$', views.orders, name='orders'),
#
#     url(r'^orders/add/$', views.add_orders, name='add_orders'),
#
#     url(r'^logout-then-login/$', auth_views.logout_then_login, name='logout_then_login'),
#
#     # форма изменения пароля
#     url(r'^password-change/$', auth_views.password_change, name='password_change'),
#     # успешная смена пароля
#     url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
#     url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
#     url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
#     url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', auth_views.password_reset_confirm,
#         name='password_reset_confirm'),
#     url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
# ]
