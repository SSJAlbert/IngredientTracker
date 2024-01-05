from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    entry_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.name.title()}, amt: {self.quantity}"



class Recipes(models.Model):
    class FoodCategory(models.TextChoices):
        Breakfast = "Breakfast"
        Lunch = "Lunch"
        Dinner = "Dinner"
        Snack = "Snack"
    name = models.CharField(max_length=30)
    ingredients = models.ForeignKey(Inventory,on_delete=models.PROTECT)
    servings = models.IntegerField(blank=True,default=1)
    food_category = models.CharField(choices=FoodCategory.choices,max_length=20,blank=True)

    def __str__(self):
        return self.name




 



