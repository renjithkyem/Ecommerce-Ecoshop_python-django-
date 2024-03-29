from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug         = models.SlugField(max_length=100, unique=True)
    description  = models.TextField(max_length=255, blank=True)
    images       = models.ImageField(upload_to='photos/products')
    price        = models.DecimalField(max_digits=10, decimal_places=2)
    stock        = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category     = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_dtae = models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)

    
    def get_url(self):
        
        return reverse('product_detail', args=[self.category.slug, self.slug])
    

    def __str__(self):
        return self.product_name