from django.db import models


class Student(models.Model):
    first_name = models.CharField(blank=True,null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True,max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField()
    phone = models.CharField(blank=True, null=True,max_length=50)
    email = models.CharField(blank=True, null=True,max_length=50)
    pay_by_parents = models.BooleanField(default=True)
    group = models.ForeignKey("group.Group", on_delete=models.SET_NULL, null=True)


class Payer(models.Model):
    first_name = models.CharField(blank=True, null=True,max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    who = models.CharField(blank=True, null=True, max_length=50)
    phone = models.CharField(blank=True, null=True, max_length=50)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)


class Speciality(models.Model):
    name = models.CharField(blank=True, null=True, max_length=50)


class Teacher(models.Model):
    first_name = models.CharField(blank=True, null=True, max_length=50)
    last_name = models.CharField(blank=True, null=True, max_length=50)
    phone = models.CharField(blank=True, null=True, max_length=50)
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True)


