from django.contrib import admin
from .models import Blog, Category

# Register your models here.
# buraya ilgili modellerimizi admin paneline dahil edicez
# tabii once importlamamız lazım

# detaylı tablo gibi gosterim icin sınıf tanımlaması yapalım

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'is_home', 'slug'] # tablo gibi gorunur kılma
    list_editable = ['is_active', 'is_home'] # editleyebilme ozelligi

    search_fields = ['title', 'description'] # arama cubugu eklemes
    # readonly_fields = ['description'] sadece okunabilir olur
    readonly_fields = ['slug']
    # burda direkt kendi filtreleme islemimizi yapabiliyoruz
    # işte programlamaları getir, mobilleri getir, active olanları getir gibi
    list_filter = ['category', 'is_active', 'is_home']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    search_fields = ['name']
    readonly_fields = ['slug']

admin.site.register(Blog, BlogAdmin) # paremetre olarak ozellestirnmeleri de verecegiz
admin.site.register(Category, CategoryAdmin)
# seklinde modellerimizi ekleriz
