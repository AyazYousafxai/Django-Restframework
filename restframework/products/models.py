from django.db import models
import decimal
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=15, default=99.99)

    @property
    def sale_price(self):
        return "%.2f" % (self.price)

    def get_discount(self):
        return self.price - 5
