from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload, about_views, contact_views

urlpatterns = [
    path("", image_upload, name="index"),
    path("admin/", admin.site.urls),
    path("about", about_views, name='about'),
    path("contact", contact_views, name='contact'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# if bool(settings.DEBUG):
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
