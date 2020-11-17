from django.db import models

# Create your models here.
CATEGORY = (
    ('E', 'Electronics'),
    ('HS', 'HomeSupplies'),
    ('B', 'Books')
)


class Product(models.Model):
    produtId =models.IntegerField(unique=True)
    productName = models.CharField(max_length = 50)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productSellerName = models.CharField(max_length = 50)
    productColor = models.CharField(max_length = 50)
    ProductCategory = models.CharField(choices=CATEGORY, max_length=2)
    productImage = models.ImageField(upload_to='images/')

class Cart(models.Model):
    product = models.ForeignKey( Product, on_delete=models.CASCADE)
    productQuantity = models.IntegerField()
