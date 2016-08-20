from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Account, Organization


class AccountInline(admin.StackedInline):
    model = Account
    fk_name = 'user'
    can_delete = False
    verbose_name_plural = 'account'


class UserAdmin(BaseUserAdmin):
    inlines = (
        AccountInline,
    )
    list_display = (
        'username',
        'email',
        'is_staff',
        'is_active',
    )
    list_editable = (
        'is_active',
        'is_staff',
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = (
        'username',
        'email',
        'first_name',
        'last_name',
    )


class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'owner',
        'is_active',
    )
    list_filter = (
        'is_active',
    )
    list_editable = (
        'is_active',
    )
    filter_horizontal = (
        'members',
        'admins',
    )
    search_fields = (
        'name',
    )
    raw_id_fields = (
        'owner',
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Organization, OrganizationAdmin)
