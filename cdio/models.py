
from django import db
from django.db import models

#Create your models here.
 
class login_record(models.Model):
    
    username=models.CharField( max_length=8,null=True)

    department=models.CharField( max_length=25,null=True)

    password=models.CharField(max_length=8,null=True)

    class Meta:
        db.table="login"
             
# class signup(models.Model):
#     username=models.CharField(max_length=8, null=True)
    
#     password=models.CharField(max_length=8, null=True)

#     class Meta:
#         db.table="signup"