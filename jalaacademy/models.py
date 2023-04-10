from django.db import models
from django_mysql.models import ListTextField
# Create your models here.

class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
     )
    emp_id = models.AutoField(primary_key=True)
    emp_fame = models.CharField(max_length=255)
    emp_lame = models.CharField(max_length=255)
    emp_email = models.CharField(max_length=1000)
    emp_phone = models.CharField(max_length = 10)
    timestamp = models.DateTimeField(blank=True)
    emp_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    emp_address = models.CharField(max_length=2000)
    emp_skills = ListTextField(
        base_field=models.CharField(max_length=1000),
        size=10,  # Maximum of 100 ids in list
    )
    emp_city = models.CharField(max_length=200)
    emp_country = models.CharField(max_length=200)