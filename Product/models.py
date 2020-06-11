from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=33)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Name: {0}, Weight: {1}, Price: {2}, Created: {3}, Updated: {4}" \
            .format(self.name, self.weight, self.price, self.created_at, self.updated_at)

    # class Meta:
    #     app_label = 'myproduct'
