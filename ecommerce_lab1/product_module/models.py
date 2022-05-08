from django.db import models

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=200)
    is_active = models.BooleanField()

class Category(models.Model):
    name = models.CharField
    is_active  = models.BooleanField()

    class Meta:
        verbose_name_plural = "Categories"

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    image_url = models.CharField(max_length=500)
    color_code = models.CharField(max_length=20)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    registered_on = models.DateTimeField()
    is_active = models.BooleanField()