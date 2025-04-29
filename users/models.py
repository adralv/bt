from django.db import models

# Create your models here.
class User(models.Model):
    username= models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    email = models.EmailField((""), max_length=250)
    password= models.CharField(max_length=250)
    graduation_year = models.IntegerField()
    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    
    