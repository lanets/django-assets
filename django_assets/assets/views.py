from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Asset
from .models import Location
from .models import Supplier


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
    extra_context = {
        'users': User.objects.all()
    }


class AssetListView(LoginRequiredMixin, ListView):
    model = Asset
    template_name = 'generic_list.html'


class LocationListView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'generic_list.html'


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'generic_list.html'
