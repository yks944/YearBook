from django.db import models

# Create your models here.
class TeacherEvents(models.Model):
    username = models.CharField(max_length=20,default=None,unique=True)
    designation = models.CharField(max_length=10,default='')
    year = models.CharField(max_length=4,default='2020')
    branch = models.CharField(max_length=10,default='')
    dob = models.DateField()
    qualification = models.TextField(max_length=30,default='')
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=10,default='')
    experience = models.TextField()
    specialization = models.TextField()
    subjects = models.TextField()

    def __str__(self):
        return self.username

class StudentEvents(models.Model):
    username = models.CharField(max_length=20,default=None,unique=True)
    enroll = models.CharField(max_length=20,default=None)
    year = models.CharField(max_length=4, default='2020')
    branch = models.CharField(max_length=10, default='')
    dob = models.DateField()
    email = models.EmailField(max_length=30)
    mobile = models.CharField(max_length=10, default='')
    address = models.TextField()
    achievements = models.TextField()

    def __str__(self):
        return self.username
