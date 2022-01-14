from django.db import models


class Pictures(models.Model):
    name = models.CharField(max_length=56)
    image = models.ImageField(upload_to="images")
