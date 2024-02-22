from django.db import models

# Create your models here.
class Book(models.Model):

    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    genre=models.CharField(max_length=20)

#python manage.py makemigrations                                   
                                             #convert ORM query to the query language

                                             #insert values into the tabel(model)
#python manage.py migrate
#modelname.objects.create(values)
#python manage.py shell
#from application.models import Modelname
#modelname.objects.create(values)
class Employee(models.Model):
    name=models.CharField(max_length=20)
    salary=models.CharField(max_length=20)
    position=models.CharField(max_length=20)
    place=models.CharField(max_length=200,null=True)


class Student(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    course=models.CharField(max_length=20)

class Person(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    job=models.CharField(max_length=20)
    
    
