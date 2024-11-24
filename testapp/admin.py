from django.contrib import admin
from . models import Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name','email', 'phone']
admin.site.register(Profile,ProfileAdmin)

# Register your models here.
