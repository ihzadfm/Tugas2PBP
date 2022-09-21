from django.db import models

class MyWatchList(models.Model):
    watched = models.TextField()
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()