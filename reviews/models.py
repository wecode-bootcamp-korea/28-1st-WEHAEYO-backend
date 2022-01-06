from django.db                 import models
from django.db.models.deletion import CASCADE

from payments.models           import Cart
from restaurants.models        import Restaurant
from users.models              import User

class Review(models.Model):
    rating      = models.DecimalField(max_digits=2, decimal_places=1)
    updated_at  = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000)
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    restaurant  = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'

class Option(models.Model):
    name  = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'options'

class MenuType(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    restaurant  = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'menu_types'

class Menu(models.Model):
    name       = models.CharField(max_length=50)
    price      = models.DecimalField(max_digits=10, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    options    = models.ManyToManyField(Option, related_name="extra_menu")
    carts      = models.ManyToManyField(Cart, related_name="menu")
    menu_types = models.ManyToManyField(MenuType, related_name="group_menu")

    class Meta:
        db_table = 'menus'

class ImageMenu(models.Model):
    url  = models.URLField(max_length=1000)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = 'image_menus'
