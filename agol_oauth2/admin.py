from django.contrib import admin
from django.contrib.auth.models import User

from .models import AGOLUserFields
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)


class AGOLUserFieldsInline(admin.StackedInline):
    model = AGOLUserFields


@admin.register(User)
class AGOLUserAdmin(UserAdmin):
    inlines = (AGOLUserFieldsInline,)
