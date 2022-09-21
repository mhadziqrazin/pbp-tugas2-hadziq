from django.db import models

class MyWatchlist(models.Model):
    watched = models.CharField(max_length=20)
    title = models.CharField(max_length=150)
    rating = models.CharField(max_length=3)
    release_date = models.CharField(max_length=40)
    review = models.TextField()