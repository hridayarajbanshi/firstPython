from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Customer(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
