from django.contrib import admin
from .views import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['username','email','password']


# Register your models here.
