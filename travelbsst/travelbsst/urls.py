from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from flex.views import home_view

from django.urls import path,re_path

from django.conf.urls import handler404
from . import views


urlpatterns = [
    path('joinUsRequest/', views.joinUsRequest, name="joinUsRequest"),
    path('contactUsRequest/', views.contactUsRequest, name="contactUsRequest"),
    path('', include('accommodation.urls')),
    url(r'^.well-known/pki-validation/89C8C03A5E8FD44929A39F310B599CAB.txt', views.firebase_messaging_sw_js),


    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r'', include(wagtail_urls)),
    re_path(r'^(?P<path>.*)/$', home_view),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]
handler404 = 'myapp.views.error_404_view'


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
