from django.db import models

# Create your models here.

class Users(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    birthday = models.CharField(max_length=50)
    birthplace = models.CharField(max_length=50)
    address_id = models.CharField(max_length=50)
    address_domisili = models.CharField(max_length=50)
    profile_img = models.CharField(max_length=500)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    flag_active = models.CharField(max_length=50)
    nik = models.CharField(max_length=100)
    npwp = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)


