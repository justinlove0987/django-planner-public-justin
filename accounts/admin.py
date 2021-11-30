from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account


class AccountAdmin(UserAdmin):
    list_display = ("email", "username", "last_login", "date_joined", "is_active")
    list_display_links = ("email",)
    
    readonly_fields = ("last_login", "date_joined")
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = () # make password read-only 
    fieldsets = () # control the layout of admin “add” and “change” pages.

admin.site.register(Account, AccountAdmin)


