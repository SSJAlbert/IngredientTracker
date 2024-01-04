from django.contrib import admin
from inventory.models import Inventory, Recipes

class InventoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Inventory, InventoryAdmin)

# Register your models here.
