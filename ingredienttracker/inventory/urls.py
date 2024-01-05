from django.urls import path
from inventory.views import InventoryListView, InventoryCreateView, RecipesListView, RecipesCreateView

from . import views

urlpatterns = [
    #path("", InventoryListView.as_view(), name="inventory-list"),
    path("inventory/", InventoryListView.as_view(), name="inventory-list"),
    path("recipes/", RecipesListView.as_view(), name="recipes-list"),
    path("create-inventory/", InventoryCreateView.as_view(), name="inventory-create"),
    path("create-recipes/", RecipesCreateView.as_view(), name="recipes-create"),

]