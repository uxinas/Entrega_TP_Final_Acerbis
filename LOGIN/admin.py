from django.contrib import admin
from .models import  * 
#from django.contrib.auth import get_user_model

admin.site.register(Login)

#list(get_user_model().objects.filter(is_superuser=True).values_list('username', flat=True))

