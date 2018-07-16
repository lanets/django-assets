from django.contrib import admin

from import_export.admin import ImportExportModelAdmin
from import_export import resources

from .models import Asset
from .models import Location
from .models import Category
from .models import Owner
from .models import Supplier


class AssetResource(resources.ModelResource):
    class Meta:
        model = Asset


class AssetAdmin(ImportExportModelAdmin):
    resource_class = AssetResource


admin.site.register(Asset, AssetAdmin)
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Owner)
admin.site.register(Supplier)
