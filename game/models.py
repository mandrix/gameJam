from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Card(model.models):
    categories = {"a": "A"}

    name = models.CharField(max_lenght = 50)
    description = models.CharField(max_lenght = 100)
    img = models.models.ImageField(upload_to="experience/images")

    label = models.CharField(
        max_length=1,
        choices=categories,
        default="a",
    )
