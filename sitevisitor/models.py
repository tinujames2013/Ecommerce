from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places= 2)
    stock = models.IntegerField()
    product_photo = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category,on_delete= models.CASCADE)
    
    def __str__(self):
        return self.name
