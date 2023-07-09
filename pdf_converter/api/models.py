from django.db import models

class Category(models.Model):
    category=models.CharField(max_length=100)

class Book(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    book=models.CharField(max_length=100)

class student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(default=18)

class excel_export(models.Model):
    excel=models.FileField(upload_to='excel/')

