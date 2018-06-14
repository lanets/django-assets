from django.conf.urls import url

from django_assets.assets import views

app_name = 'assets'

urlpatterns = [

    url(
        r'^$',
        views.HomeView.as_view(),
        name="home"
    ),

]
