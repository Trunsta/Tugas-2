from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date = models.DateField(default = datetime.now())
    title = models.TextField()
    description = models.TextField()