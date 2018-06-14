from django.db import models
from django.utils.translation import ugettext_lazy as _


class Supplier(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=200)
    contact = models.CharField(verbose_name=_("Contact"), max_length=200)
    account_id = models.CharField(verbose_name=_("Account ID"), max_length=200)

    # Creation and last modifications dates
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
