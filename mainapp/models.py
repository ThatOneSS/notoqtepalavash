from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image= models.URLField(blank=True , null=True)
    status= models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image= models.URLField(blank=True , null=True)

    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=100, unique=True)
    working_hours = models.CharField(max_length=100, default='9:00 - 22:00 PM')
    image= models.URLField(blank=True , null=True)
    address=models.URLField()

    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name