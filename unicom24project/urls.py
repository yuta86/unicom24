# from django.conf.urls import include, url
# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static
# from account import views
#
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls), name='admin'),
#     url(r'^$', views.home, name='home'),
#     url(r'^account/', include('account.urls')),
#     #url(r'^', include('business.urls', namespace='business')),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls import url
from django.contrib import admin
from account import views, apis
from django.conf.urls import include

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^$', views.home, name='home'),

                  url(r'^account/sign-in/$', auth_views.login, {'template_name': 'account/sign_in.html'},
                      name='account_sign_in'),
                  url(r'^account/sign-out', auth_views.logout, {'next_page': '/'}, name='account_sign_out'),
                  url(r'^account/$', views.account_home, name='account_home'),
                  url(r'^account/sign-up', views.account_sign_up, name='account_sign_up'),
                  url(r'^account/account/$', views.account_account, name='account_account'),
                  url(r'^account/orders/$', views.account_orders, name='account_orders'),
                  url(r'^account/orders/add/$', views.account_add_orders, name='account_add_orders'),
                  url(r'^account/orders/edit/(?P<order_id>\d+)/$', views.account_edit_orders,
                      name='account_edit_orders'),

                  # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^api-auth/v1/profiles/$', views.ProfileListView.as_view(), name='profiles_list'),
                  url(r'^api-auth/v1/profiles/(?P<pk>\d+)/$', views.ProfileDatailView.as_view(), name='profile_detail'),

                  url(r'^api-auth/v1/offers/$', views.OfferListView.as_view(), name='offers_list'),
                  url(r'^api-auth/v1/offers/(?P<pk>\d+)/$', views.OfferDatailView.as_view(), name='offer_detail'),

                  url(r'^api-auth/v1/partner/$', views.PartnerListView.as_view(), name='partner_list'),
                  url(r'^api-auth/v1/partner/(?P<pk>\d+)/$', views.PartnerDatailView.as_view(), name='partner_detail'),


# другой вариант api
                  url(r'^api/v1/profiles/$', apis.client_get_profiles),
                  url(r'^api/v1/request/(?P<request_id>\d+)/$', apis.client_get_request),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
