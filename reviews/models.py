from django.db                 import models
from django.core.validators    import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE

from payments.models           import Cart
from restaurants.models        import Restaurant
from users.models              import User

# Create your models here.
class Review(models.Model):
    rating      = models.IntegerField(validators=[MinValueValidator(1),
                                                  MaxValueValidator(5)])
    updated_at  = models.DateTimeField(auto_now=True)
    description = models.TextField(max_length=1000)
    user        = models.ForeignKey(User, on_delete=CASCADE)
    restaurant  = models.ForeignKey(Restaurant, on_delete=CASCADE)

    class Meta:
        db_table = 'reviews'

class Option(models.Model):
    name  = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    class Meta:
        db_table = 'options'


class MenuType(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)

    class Meta:
        db_table = 'menu_types'


class Menu(models.Model):
    name       = models.CharField(max_length=50)
    price      = models.DecimalField(max_digits=1000, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=CASCADE)
    options    = models.ManyToManyField(Option)
    carts      = models.ManyToManyField(Cart)
    menu_types = models.ManyToManyField(MenuType)

    class Meta:
        db_table = 'menus'

class ImageMenu(models.Model):
    url  = models.URLField(max_length=1000)
    menu = models.ForeignKey(Menu, on_delete=CASCADE)

    class Meta:
        db_table = 'image_menus' 