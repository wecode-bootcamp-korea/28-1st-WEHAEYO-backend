from django.db          import models

from restaurants.models import Restaurant

# Create your models here.
class User(models.Model):
    name         = models.CharField(max_length=50)
    password     = models.CharField(max_length=128)
    email        = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    wishilists   = models.ManyToManyField(Restaurant, related_name="shopper")

    class Meta:
        db_table = 'users'
