from django.contrib import admin
from .models import Blog

# Register your models here.
class AuthAdmin(admin.ModelAdmin):
    list_display = ('title','status','author','created_on')

admin.site.register(Blog,AuthAdmin)


