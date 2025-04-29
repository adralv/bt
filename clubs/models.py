from django.db import models

# Create your models here.
class Club(models.Model):
    club_name= models.CharField(max_length=100)
    club_members = models.IntegerField()
    description = models.TextField(blank=True)
    room_number = models.IntegerField()
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    email= models.EmailField((""), max_length=250)
    teacher=models.CharField(max_length=100)
    actvities=models.ArrayField(base_field=)