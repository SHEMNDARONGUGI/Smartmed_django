from typing import Any
from django.db import models

# table name is Member

class Member(models.Model): 
    fullname = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    yob =models.DateField()
    
    def __str__(self):
        return self.fullname
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    serial_no = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    quantity = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    date = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    
class User(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password  = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.name   
    
# # class ImageModel(models.Model):
#     image = models.ImageField(upload_to='images/')
#     title = models.CharField(max_length=50)
#     price = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title