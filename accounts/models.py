from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager,User
# Create your models here.
class manage(BaseUserManager):
    def create_user(self,username,password,utype):
        user = self.model(username=username)
        user.utype=utype
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,username,password):
        user = self.create_user(username,password,utype="Admin")
        user.is_admin =True
        user.is_staff = True
        user.is_superuser=True
        user.save()
        return user
class CustomUser(AbstractUser):
    username = models.CharField(max_length=20,unique=True)
    utype = models.CharField(max_length=10)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects=manage()
class Profile(models.Model):
    enroll_id = models.TextField(max_length=15,default='')
    email = models.EmailField(unique=True,max_length=60)
    address = models.TextField(max_length=100,default='')
    mobile = models.TextField(max_length=10,default='')
    profile = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
