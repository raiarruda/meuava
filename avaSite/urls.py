from django.conf.urls import  include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^', include('avaSite.core.urls', namespace='core')),
    url(r'^conta/', include('avaSite.accounts.urls', namespace='accounts')),
 #   url(r'^cursos/', include('avaSite.activities.urls', namespace='activities')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )