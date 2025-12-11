from django.contrib import admin
from .models import Blog  

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User, Permission

from django.contrib.auth.admin import UserAdmin
from .forms import EmailAuthenticationForm


from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .forms import CustomAuthenticationForm  


admin.site.register(Blog)
admin.site.register(Permission)


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email',)}), 
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class CustomAdminSite(admin.AdminSite):
    login_form = EmailAuthenticationForm

admin_site = CustomAdminSite()
admin_site.register(User, UserAdmin)

admin.site.login_form = CustomAuthenticationForm  
