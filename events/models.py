from django.db import models
from clubs.models import Club

# Create your models here.
class Announcements(models.Model):
    # club_id = Put Club ID from club model
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    title = models.CharField()
    description = models.CharField()
    date = models.DateTimeField()
    location = models.IntegerField()
    
    
    def __str__(self):
        return self.date.strftime('%A, %B %d, %I:%M %p')

    # publisher = Put User ID
    
