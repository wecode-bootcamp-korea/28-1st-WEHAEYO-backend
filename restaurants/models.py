from django.db                 import models
from django.db.models.deletion import CASCADE, PROTECT

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories' 

class Restaurant(models.Model):
    name      = models.CharField(max_length=50)
    category  = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    phone     = models.CharField(max_length=100, null=True)
    address   = models.CharField(max_length=1000, null=True)

    class Meta:
        db_table = 'restaurants'

class ImageCategory(models.Model):
    url      = models.URLField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'image_categories' 

class ImageRestaurant(models.Model):
    url        = models.URLField(max_length=1000)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'image_restaurants' 