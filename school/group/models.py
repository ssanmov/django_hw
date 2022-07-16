from django.db import models


# Create your models here.

class Group(models.Model):
    name = models.CharField(blank=True,null=True, max_length=50)
    start_date = models.DateField()
    start_time = models.TimeField()
    teacher = models.ForeignKey("members.Teacher", on_delete=models.SET_NULL, null=True)
    speciality = models.ForeignKey("members.Speciality", on_delete=models.SET_NULL, null=True)

class Group_history(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)
    start_date = models.DateField()
    start_time = models.TimeField()
    teacher = models.ForeignKey("members.Teacher", on_delete=models.SET_NULL, null=True)
    speciality = models.ForeignKey("members.Speciality", on_delete=models.SET_NULL, null=True)
    created = models.DateField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True)


