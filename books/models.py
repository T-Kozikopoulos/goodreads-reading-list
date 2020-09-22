from django.db import models
from django.contrib.auth.models import User


# Creating the model for the 'book' objects.
class Book(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=80, default='')
    author = models.CharField(max_length=80, default='')
    # When deleting the user, also delete everything related to them to save space on the database.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
