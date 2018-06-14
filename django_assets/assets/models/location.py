from django.db import models
from django.utils.translation import ugettext_lazy as _


class Location(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=200)

    # Creation and last modifications dates
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
