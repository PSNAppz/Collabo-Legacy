from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls import include, url
from qr_code import urls as qr_code_urls
from filebrowser.sites import site

#from saloonapp.views import saloonapp
app_name='accounts'

admin.site.site_header = "COLLABO EVENT ADMIN"
admin.site.site_title = "EVENT ADMIN PORTAL"
admin.site.index_title = "Welcome to Event Admin Portal"


urlpatterns = [

    path('', include('collabo_events.urls')),

    path('api/', include('events_api.urls')),

    path('auth/', include('events_api.urls')),
    path('auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^qr_code/', include(qr_code_urls, namespace="qr_code")),
    #path('mob/', include('drf_accountkit.urls')),
    path('accounts/',include('django.contrib.auth.urls')),

    #url(r'^booking/', include('booking.urls')),
    #url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS

    #url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),




    #path('accounts/', include('django.contrib.auth.urls')),
    #url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS

    #url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    #path('admin/', admin.site.urls),
    url(r'^admin/', (admin.site.urls)),
    url(r'^admin/filebrowser/', (site.urls)),


    #url(r'^admin/', include(admin.site.urls)),
    #path('accounts/signup/', saloonapp.SignUpView.as_view(), name='signup'),
    #path('accounts/signup/customer/', operators.CustomerSignUpView.as_view(), name='customer_signup'),
    #path('accounts/signup/owner/', saloonapp.OwnerSignUpView.as_view(), name='owner_signup'),
    # path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )



