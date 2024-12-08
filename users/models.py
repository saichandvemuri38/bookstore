from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    usertype=models.CharField(max_length=255)
    library_name = models.CharField(max_length=255, unique=True)
    dob = models.DateField()
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class AddLibraryModel(models.Model):
    name = models.CharField(max_length=255, unique=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip4 = models.CharField(max_length=255)

class AddBookModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    price = models.IntegerField(max_length=255)
    quantity = models.IntegerField(max_length=255)

class CheckInModel(models.Model):
    bookId = models.IntegerField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    price = models.IntegerField(max_length=255)
    quantity = models.IntegerField(max_length=255)
    libraryname = models.CharField(max_length=255)
    userId = models.IntegerField(max_length=255)
    status = models.CharField(max_length=255)
    