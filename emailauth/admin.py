from django.contrib.admin.options import ModelAdmin
from django.contrib.admin import site
from models import UserEmail

class UserEmailAdmin(ModelAdmin):
    list_display = ['user', 'email', 'default', 'verification_key']
    
site.register(UserEmail, UserEmailAdmin)