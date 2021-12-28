from django.db                 import models
from django.core.validators    import MinValueValidator, MaxValueValidator
from django.db.models.deletion import CASCADE

from users.models              import User

# Create your models here.
class Cart(models.Model):
    quantity = models.IntegerField(validators=[MinValueValidator(1),
                                              MaxValueValidator(99)])
    user    = models.ForeignKey(User, on_delete=CASCADE)
                                              
    class Meta:
        db_table = 'carts'

class Order(models.Model):
    payment_method = models.CharField(max_length=200)
    total_price    = models.DecimalField(max_digits=1000, decimal_places=2)
    cart           = models.ForeignKey(Cart,on_delete=CASCADE)

    class Meta:
        db_table = 'orders' 