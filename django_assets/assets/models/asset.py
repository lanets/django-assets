from django.db import models
from django.utils.translation import ugettext_lazy as _

from .location import Location
from .category import Category
from .owner import Owner
from .supplier import Supplier


class Asset(models.Model):

    ASSET_STATES = [
        ('REPA', _('En réparation')),
        ('INUSE', _("En cours d'utilisation")),
        ('HS', _('Hors Service')),
        ('DFCT', _('Défectueu'))
    ]

    name = models.CharField(verbose_name=_("Name"), max_length=200)

    value = models.IntegerField()
    acquisition_date = models.DateField(auto_now=True)

    state = models.CharField(
        verbose_name=_("State"),
        max_length=5,
        choices=ASSET_STATES,
    )

    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    # Creation and last modifications dates
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
