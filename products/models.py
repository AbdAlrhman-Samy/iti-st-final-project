from turtle import title
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "Categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    thumbnail = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = "Products"
        verbose_name = "Product"
        verbose_name_plural = "Products"
