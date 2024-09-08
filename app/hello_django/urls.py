from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload import views 

urlpatterns = [
    path("", views.image_upload, name="index"),
    path("admin/", admin.site.urls),
    path("about", views.about_views, name='about'),
    path("contact", views.contact_views, name='contact'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



