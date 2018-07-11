# -*- coding: utf-8 -*-
from enum import Enum

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .location import Location
from .category import Category
from .owner import Owner
from .supplier import Supplier


class AssetStates(Enum):
    REPA = _('En réparation')
    INUSE = _("En cours d'utilisation")
    HS = _('Hors Service')
    DFCT = _('Défectueux')
    OK = _('Fonctionnel')


class Asset(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=200)

    value = models.DecimalField(max_digits=19, decimal_places=2)
    acquisition_date = models.DateField()

    state = models.CharField(
        verbose_name=_("State"),
        max_length=5,
        choices=[(state.name, state.value) for state in AssetStates],
        default='OK',
    )

    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField(Category, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)

    # Creation and last modifications dates
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
