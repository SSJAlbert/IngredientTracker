from django.urls import path
from inventory.views import InventoryListView, InventoryCreateView

from . import views

urlpatterns = [
    #path("", InventoryListView.as_view(), name="inventory-list"),
    path("", InventoryListView.as_view(), name="inventory-list"),
    path("create/", InventoryCreateView.as_view(), name="inventory-create"),

]