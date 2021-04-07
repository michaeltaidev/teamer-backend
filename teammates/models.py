from django.db import models

class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

class Teammates(models.Model):
    TeammateId = models.AutoField(primary_key=True)
    TeammateName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    JoinDate = models.DateField()
    ProfilePicFileName = models.CharField(max_length=300)