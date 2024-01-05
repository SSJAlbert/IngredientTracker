from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.db import models
from django.urls import reverse_lazy

from inventory.models import Inventory, Recipes

def home_screen_view(request):

    context = {}
    #context['some_string'] = "this is some string that I'm passing to the view"
    #context['some_number'] = 12345

    # context = {
    #     'some_string': "this is some string that I'm passing to the view",
    #     'some_number': 12345,
    # }

    list_of_values = []
    list_of_values.append("first entry")
    list_of_values.append("second entry")
    list_of_values.append("third entry")
    list_of_values.append("fourth entry")
    context['list_of_values'] = list_of_values
    return render(request, "inventory/home.html", context)

class InventoryListView(ListView):
    model = Inventory
    paginate_by = 20

    template_name = 'inventory_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    
class RecipesListView(ListView):
    model = Recipes
    paginate_by = 20

    template_name = 'recipes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
    

class InventoryCreateView(CreateView):
    model = Inventory
    paginate_by = 20
    fields = ['name','quantity','expiry_date']
    success_url = reverse_lazy("inventory-list")

    template_name = 'inventory_create.html'

    def dispatch(self, request, *args, **kwargs):
         self.request = request
         return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.entry_date = models.DateTimeField(auto_now_add=True)
        obj.save()
        return super().form_valid(form)
    
class RecipesCreateView(CreateView):
    model = Recipes
    paginate_by = 20
    fields = ['name','ingredients','servings','food_category']
    success_url = reverse_lazy("recipes-list")

    template_name = 'recipes_create.html'

    def dispatch(self, request, *args, **kwargs):
         self.request = request
         return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super().form_valid(form)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["now"] = timezone.now()
    #     return context


