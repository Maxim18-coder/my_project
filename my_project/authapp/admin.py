from django.contrib import admin
from .models import User, Role, Permission, UserRole


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('username',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('resource', 'action', 'role')
    search_fields = ('resource', 'action', 'role__name')
    list_filter = ('role',)
    ordering = ('resource',)


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__username', 'role__name')
    list_filter = ('role',)
    ordering = ('user',)