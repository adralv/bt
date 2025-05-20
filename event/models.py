from django.db import models
from clubs.models import Club
# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=500)
    public_event = models.BooleanField(default=False)
    club=models.ForeignKey(Club,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    date=models.DateField()
    choices =[('Tournament', 'Tournament'),('Bake Sale', 'Bake Sale'),('School Event', 'School Event')]
    type = models.CharField(
        choices= choices,
        default ="Bake Sale")
    type2 = models.CharField(choices= [('Round Robin', 'Round Robin'),('Single Elimination', 'Single Elimination'),('Double Elimination', 'Double Elimination')], default=None, null=True)
    