from django.db import models


class Asset(models.Model):
    name_text = models.CharField(max_length=250)
    quantity = models.