from django.db import models

# Create your models here.

class Products(models.Model):
    SHIRT_CHOICES = [
    ('CG', 'Convenience Goods'),
    ('SHG', 'Shopping Goods'),
    ('SG', 'Specialty Goods'),
    ]
    name = models.CharField(max_length=125, unique=True)
    description = models.TextField(max_length=500)
    category = models.CharField(max_length=50, choices=SHIRT_CHOICES)
    picture = models.ImageField(upload_to='products/images')
    amount = models.IntegerField(default=0)
    price = models.DecimalField(default=0.00, max_digits=7 , decimal_places=2)
    production_date = models.DateField(auto_now_add=True)
    is_new = models.BinaryField(default=False)
    certificate = models.FileField(upload_to='products/files')
    rating = models.DecimalField(default=0.0, blank=True, max_digits=2, decimal_places=1)
    view_link = models.URLField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'company_products'
        ordering = ['name']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'