import imp
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Search(models.Model):
    query=models.CharField(max_length=25)
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    create_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.query
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    phone=models.CharField(max_length=25)
    subject=models.CharField(max_length=25)
    
    

    def __str__(self):
        return self.name


class Subscriber(models.Model):
    email=models.EmailField()

    def __str__(self):
        return self.email
class Feedback(models.Model):
    mail=models.EmailField()
    msg=models.CharField(max_length=100)

    def __str__(self):
        return self.msg