from django.contrib import admin

# Register your models here.
from app.models import *

admin.site.register(TOPIC)

admin.site.register(WEBPAGE)

admin.site.register(ACCESS_RECORD)
