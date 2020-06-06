from django.db import models
from django.utils.translation import gettext as _
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

class Manufacturer(models.Model):
    name = models.CharField(max_length=125, unique=True)
    description = models.TextField(max_length=500)

class Car(models.Model):
    name = models.CharField(max_length=125, unique=True)
    production_date = models.DateField(auto_now_add=True)
    is_new = models.BinaryField(default=False)
    manufacturer = models.ForeignKey("modelsTask.Manufacturer", verbose_name=_("Manufacturer"), on_delete=models.CASCADE, null = True, blank = True)

class Book(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    description = models.TextField(_("Description"), blank=True)
    price = models.DecimalField(_("Price"), max_digits=5, decimal_places=2)
    page_count = models.IntegerField(_("Page count"))
    cover_image = models.ImageField(_("Cover image"), upload_to="partials/images")
    author = models.ForeignKey("modelsTask.Author", verbose_name=_("Author"), on_delete=models.CASCADE)

class Author(models.Model):
    fullname = models.CharField(_("Fullname"), max_length=50)
    image = models.ImageField(_("Image"), upload_to="partials/images")
    gender = models.BinaryField(_("Gender"))
    date_of_birthday = models.DateField(_("Date of birthday"), auto_now_add=True)
    nationality = models.CharField(_("Nationality"), max_length=50)
    info = models.TextField(_("Info"), default="")

class Category(models.Model):
    title = models.TextField(_("Title"), default="")
    books = models.ManyToManyField("modelsTask.Book", verbose_name=_("Book"))


    