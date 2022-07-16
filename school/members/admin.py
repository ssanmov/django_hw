from django.contrib import admin

from .models import *

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Payer)
admin.site.register(Speciality)