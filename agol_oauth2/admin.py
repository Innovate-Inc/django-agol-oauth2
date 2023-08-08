from django.contrib import admin
from django.contrib.auth.models import User

from .models import AGOLUserFields
from django.contrib.auth.admin import UserAdmin


class AGOLUserFieldsInline(admin.StackedInline):
    model = AGOLUserFields

RegisteredUserAdmin = admin.site._registry.get(User)
admin.site.unregister(User)

@admin.register(User)
class AGOLUserAdmin(UserAdmin):
    inlines = RegisteredUserAdmin.inlines + (AGOLUserFieldsInline,)
