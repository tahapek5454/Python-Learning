from unicodedata import name
from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Film Adi')
    description = models.TextField(verbose_name='Film Aciklamasi')
    image = models.CharField(max_length=50, verbose_name='Film Fotografi')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Yukleme Tarihi')
    isPublished = models.BooleanField(default=True)
   


    def __str__(self) -> str:
        return self.name
    
    def get_image_path(self):
        return '/img/'+ self.image

