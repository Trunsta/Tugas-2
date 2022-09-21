from logging.handlers import RotatingFileHandler
from django.db import models

# Create your models here.
class WatchListAttribute(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()