from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe
# bu bzie html kodlarıyla stringi ayırıyor

# Register your models here.
# buraya ilgili modellerimizi admin paneline dahil edicez
# tabii once importlamamız lazım

# detaylı tablo gibi gosterim icin sınıf tanımlaması yapalım

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'is_home', 'slug', 'selected_categories'] # tablo gibi gorunur kılma
    # buraya ya tablo prop ları geli ya da fonksiyon gelir
    list_editable = ['is_active', 'is_home'] # editleyebilme ozelligi

    search_fields = ['title', 'description'] # arama cubugu eklemes
    # readonly_fields = ['description'] sadece okunabilir olur
    readonly_fields = ['slug']
    # burda direkt kendi filtreleme islemimizi yapabiliyoruz
    # işte programlamaları getir, mobilleri getir, active olanları getir gibi
    # many to many e geccktik filterdan category i cikaricem
    list_filter = ['categories', 'is_active', 'is_home']

    def selected_categories(self,obj):
        html = "<ul>"
        
        for category in obj.categories.all():
            # objenin categories degiskenindeki veriler listeo olacagindan boyle aldı
            html += "<li> "+category.name+" </li>"
        
        html += " </ul>"
        return mark_safe(html)



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    search_fields = ['name']
    readonly_fields = ['slug']

admin.site.register(Blog, BlogAdmin) # paremetre olarak ozellestirnmeleri de verecegiz
admin.site.register(Category, CategoryAdmin)
# seklinde modellerimizi ekleriz
