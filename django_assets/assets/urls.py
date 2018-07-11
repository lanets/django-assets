from django.conf.urls import url
from django.urls import path

from django_assets.assets import views

app_name = 'assets'

urlpatterns = [

    url(
        r'^$',
        views.HomeView.as_view(),
        name="home"
    ),

    path('asset', views.AssetListView.as_view(), name='asset-list'),
    path('location', views.LocationListView.as_view(), name='location-list'),
    path('supplier', views.SupplierListView.as_view(), name='supplier-list'),

]
