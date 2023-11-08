from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100)


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=100)


class Student(models.Model):
    first_name = models.CharField(default="", max_length=100)
    middle_name = models.CharField(default="", max_length=100)
    last_name = models.CharField(default="", max_length=100)
    age = models.IntegerField(default=18)
    father_name = models.CharField(default="", max_length=100)
    email = models.EmailField(default="")
    mobile_no = models.CharField(default="", max_length=15)
    gender = models.CharField(default="", max_length=20)
    hobbies = models.CharField(default="", max_length=200)
    country_name = models.CharField(default="", max_length=200)
    about = models.CharField(default="", max_length=250)
