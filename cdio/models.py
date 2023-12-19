
from django import db
from django.db import models

#Create your models here.
 
class RegUser(models.Model):
    
    username=models.CharField( max_length=50,null=True)

    department=models.CharField( max_length=50,null=True)

    password=models.CharField(max_length=50,null=True)

    con_password=models.CharField(max_length=50,null=True)



    class Meta:
        db.table="login"
             
# class signup(models.Model):
#     username=models.CharField(max_length=8, null=True)
    
#     password=models.CharField(max_length=8, null=True)

#     class Meta:
#         db.table="signup"