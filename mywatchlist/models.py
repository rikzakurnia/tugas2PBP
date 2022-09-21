from pyexpat import model
from django.db import models

# Create your models here.
class MovieWatchList(models.Model):
    status_watched = models.BooleanField(default=False)
    judul = models.CharField(max_length=50)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.URLField()
    