from django.contrib import admin

# Register your models here.
from .models import Appointment,Blogs


admin.site.register(Appointment)
admin.site.register(Blogs)