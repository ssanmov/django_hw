from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Lesson)
admin.site.register(Theme)
admin.site.register(Lesson_student)

