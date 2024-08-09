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
    phone = models.CharField(max_length = 10, null = False, blank = True)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class BloodReq(models.Model):
    title = models.CharField(max_length = 50) 
  
    bloodChoice = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )
    bloodGroup = models.CharField(choices=bloodChoice, max_length = 10) 
    hospitalName = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    date = models.DateField()


    def __str__(self):
        return self.title
