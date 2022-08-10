from django.contrib import admin
from .models import Todo

# Register your models here.

class MyAdmin(admin.ModelAdmin):
    list_display = ('title','created','completed')

admin.site.register(Todo,MyAdmin)
