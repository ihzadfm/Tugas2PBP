from django.db import models

class MyWatchList(models.Model):
    watched = models.TextField()
    movie_title = models.CharField(max_length=50)
    movie_rating = models.FloatField()
    movie_release_date = models.TextField()
    movie_review = models.TextField()