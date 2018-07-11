from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

from .models import Asset
from .models import Location
from .models import Supplier


class HomeView(TemplateView):
    template_name = "home.html"
    extra_context = {
        'users': User.objects.all()
    }


class AssetListView(ListView):
    model = Asset
    template_name = 'generic_list.html'


class LocationListView(ListView):
    model = Location
    template_name = 'generic_list.html'


class SupplierListView(ListView):
    model = Supplier
    template_name = 'generic_list.html'
