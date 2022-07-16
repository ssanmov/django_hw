from django.db import models
# Create your models here.

class Theme(models.Model):
    name = models.CharField(blank=True,null=True,max_length=50)


class Lesson(models.Model):
    group = models.ForeignKey("group.Group", on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    is_active = models.BooleanField(default=True)
    comment = models.CharField(max_length=100)
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True)

class Lesson_student(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey("members.Student", on_delete=models.SET_NULL, null=True)
    homework_done = models.BooleanField(blank=True,null=True)
    is_available = models.BooleanField(blank=True, null=True)




