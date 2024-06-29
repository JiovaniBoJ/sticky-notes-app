# This is the sticky_notesapp models.py

from django.db import models

# Create your models here.
class User(models.Model):

    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="uploads", default="a.png")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return self.name
