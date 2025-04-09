from django.db import models
from clubs.models import Club

# Create your models here.
class Event(models.model):
    # club_id = Put Club ID from club model
    title = models.CharField()
    description = models.CharField()
    date = models.DateTimeField()
    location = models.IntegerField()
    # publisher = Put User ID
    