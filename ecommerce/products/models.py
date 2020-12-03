from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.SlugField(max_length=200,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.categoryname)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.categoryname

class ColorVariant(models.Model):
    colorid = models.AutoField(primary_key=True)
    colorname = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.colorname

class QuantityVariant(models.Model):
    quantityid = models.AutoField(primary_key=True)
    quantityname = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.quantityname

class SizeVariant(models.Model):
    sizeid = models.AutoField(primary_key=True)
    sizevalue = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return self.sizevalue

class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    productname = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products')
    price = models.CharField(max_length=10)
    description = models.CharField(max_length=500)
    stock = models.IntegerField()

    quantitytype = models.ForeignKey(QuantityVariant,on_delete=models.PROTECT,blank=True,null=True)
    colortype = models.ForeignKey(ColorVariant,on_delete=models.PROTECT,blank=True,null=True)
    sizetype = models.ForeignKey(SizeVariant,on_delete=models.PROTECT,blank=True,null=True)

    def __str__(self):
        return self.productname

class ProductImages(models.Model):
    imageid = models.AutoField(primary_key=True)
    productid = models.ForeignKey(Product,on_delete=models.CASCADE)
    productimage = models.ImageField(upload_to='products')