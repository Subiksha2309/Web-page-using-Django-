from django.db import models

    
class Category(models.Model):
        name = models.CharField(max_length=100)
        
def __str__(self):  
        return self.name


class FoodRecipe(models.Model):
    CATEGORY_CHOICES = [
        ('VEG', 'Vegetarian'),
        ('NON-VEG', 'Non-Vegetarian'),
    ]

    name = models.CharField(max_length=100, unique=True)
    img_url=models.URLField(null=True)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    
    
    def __str__(self):  
        return self.name
    
