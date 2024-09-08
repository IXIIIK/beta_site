from django.contrib import admin
from .models import PostModel, PostImg

# Register your models here.
admin.site.register(PostModel)
admin.site.register(PostImg)