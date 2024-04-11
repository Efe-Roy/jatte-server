from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'email',
        'is_admin',
        'is_rider',
        'is_vendor',
        'is_client',
        'is_active',
        'is_staff',
        'is_superuser',
    ]
    list_filter = ['is_client', 'is_vendor', 'is_rider']
    search_fields = ['name']

admin.site.register(User, UserAdmin)