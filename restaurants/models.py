from django.db                 import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'categories' 

class Restaurant(models.Model):
    name     = models.CharField(max_length=50)
    category = models.ForeignKey(Category,on_delete=CASCADE)


    class Meta:
        db_table = 'restaurants'

class ImageCategory(models.Model):
    url      = models.URLField(max_length=1000)
    category = models.ForeignKey(Category,on_delete=CASCADE)

    class Meta:
        db_table = 'image_categories' 

class ImageRestaurant(models.Model):
    url        = models.URLField(max_length=1000)
    restaurant = models.ForeignKey(Restaurant,on_delete=CASCADE)

    class Meta:
        db_table = 'image_restaurants' 