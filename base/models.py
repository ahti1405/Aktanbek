from django.db import models


    
class Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='static/img/category')

    def __str__(self):
        return self.name




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    img = models.ImageField(null=False, blank=False, upload_to='static/img/product/')
    table = models.FileField(null=True, blank=True, upload_to='data/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

