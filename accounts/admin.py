from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

from .forms import ThisUserChangeForm,ThisUserCreationForm
from .models import ThisUser

class ThisAdminUser(UserAdmin):
    add_form = ThisUserCreationForm
    form = ThisUserChangeForm
    model = ThisUser
    list_display = (
        'username',
        'email',
        'is_staff',
        'is_active',
        'is_superuser',
    )

    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'name',
            ),
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                'name',
            ),
        }),
    )

admin.site.register(ThisUser,ThisAdminUser)
 