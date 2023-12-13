from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Addition info',
            {
                'fields': ('name', 'platform'),
            }
        ),
    )


# fields = list(UserAdmin.fieldsets)
# fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'name', 'platform')})
# fieldsets = tuple(fields)

admin.site.register(NewUser, CustomUserAdmin)
