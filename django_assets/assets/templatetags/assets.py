# -*- coding: utf-8 -*-
import inspect

from django import template
from django.db.models import Sum, Count, ManyToManyField
from ..models import Asset, AssetStates
from ..models import Location
from ..models import Supplier

register = template.Library()


@register.simple_tag
def asset_count():
    return Asset.objects.count()


@register.simple_tag
def assets_value():
    return Asset.objects.aggregate(
        value=Sum('value')
    )['value'] or 0


@register.simple_tag
def location_count():
    return Location.objects.count()


@register.simple_tag
def supplier_count():
    return Supplier.objects.count()


@register.simple_tag
def assets_states():
    return {
        AssetStates[state['state']].value: state['count']
        for state in Asset.objects.values('state').annotate(
            count=Count('state')
        )
    }


@register.simple_tag
def get_meta(**kwargs):
    model = kwargs.get('model')
    meta = model._meta
    return {
        'meta': meta,
        'name': model.__class__.__name__,
        'fields': meta._get_fields(reverse=False),
    }


@register.filter(name='getfield')
def getfield(object, field):
    value = object.__getattribute__(field.name)
    if isinstance(field, ManyToManyField):
        if value.count() == 0:
            value = ''
        else:
            values = [str(obj) for obj in value.all()]
            value = ", ".join(values)
    return value
