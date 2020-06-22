from django.db import models
from django.utils import timezone


# Create your models here.
class GhostModel(models.Model):
    CHOICES = (('B', 'Boast'), ('R', 'Roast'))

    text = models.CharField(max_length=280)
    boast_or_roast = models.CharField(
        choices=CHOICES, max_length=5, null=False)
    up_vote = models.PositiveIntegerField(default=0)
    down_vote = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.boast_or_roast
