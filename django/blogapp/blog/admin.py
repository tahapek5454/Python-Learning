from django.contrib import admin
from .models import Blog, Category

# Register your models here.
# buraya ilgili modellerimizi admin paneline dahil edicez
# tabii once importlamamız lazım

# detaylı tablo gibi gosterim icin sınıf tanımlaması yapalım

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'is_home'] # tablo gibi gorunur kılma
    list_editable = ['is_active', 'is_home'] # editleyebilme ozelligi

    search_fields = ['title', 'description'] # arama cubugu eklemes
    # readonly_fields = ['description'] sadece okunabilir olur

admin.site.register(Blog, BlogAdmin) # paremetre olarak ozellestirnmeleri de verecegiz
admin.site.register(Category)
# seklinde modellerimizi ekleriz
