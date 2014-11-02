from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import models
# Register your models here.
admin.site.unregister(models.User)
admin.site.register(models.User, UserAdmin)


class UserProfileInline(admin.StackedInline):
    model = models.UserProfile
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = (UserProfileInline,)
