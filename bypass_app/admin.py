from django.contrib import admin
from .models import *
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name','is_active','is_staff']

admin.site.register(Account, AccountAdmin)

# Register your models here.
