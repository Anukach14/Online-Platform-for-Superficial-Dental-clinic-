from django.contrib import admin

# Register your models here.
from .models import Appointment,Blogs,Contact


admin.site.register(Appointment)
admin.site.register(Blogs)
admin.site.register(Contact)
