from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Task)
admin.site.register(Task_Date)
admin.site.register(History)