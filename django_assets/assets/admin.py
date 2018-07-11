from django.contrib import admin
from .models import Asset
from .models import Location
from .models import Category
from .models import Owner
from .models import Supplier

admin.site.register(Asset)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Owner)
admin.site.register(Supplier)
