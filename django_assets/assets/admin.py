from django.contrib import admin
from .models import Asset
from .models import Location
from .models import Category
from .models import Owner
from .models import Supplier

admin.register(Asset)
admin.register(Location)
admin.register(Category)
admin.register(Owner)
admin.register(Supplier)
