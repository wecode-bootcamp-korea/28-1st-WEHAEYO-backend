from django.db                 import models
from django.db.models.deletion import CASCADE

from users.models              import User

class Cart(models.Model):
    quantity     = models.IntegerField(default=0)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
                                              
    class Meta:
        db_table = 'carts'

class Order(models.Model):
    payment_method = models.CharField(max_length=200)
    total_price    = models.DecimalField(max_digits=10, decimal_places=2)
    cart           = models.ForeignKey(Cart, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders' 