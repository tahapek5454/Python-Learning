from statistics import mode
from turtle import title
from xml.parsers.expat import model
from django.db import models

# Create your models here.

# model bizim databaseimizdeki tablolara dek dusuyor

# gecen yaptıgımız views icersindeki data dict ini buraya koyalım
# ve onu veri tabanına baglayalım

class Blog (models.Model):
    # id otomatik veriliyor
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    description = models.TextField(null=True)


class Category (models.Model):
    name = models.CharField(max_length=150)
