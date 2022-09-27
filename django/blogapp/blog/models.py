from distutils.command.upload import upload
import this
from django.db import models
from django.utils.text import slugify

# Create your models here.

# not : admin paneline gitmede createsuperuser ile user olusturmalısın

# model bizim databaseimizdeki tablolara dek dusuyor

# gecen yaptıgımız views icersindeki data dict ini buraya koyalım
# ve onu veri tabanına baglayalım


# once migratin olusturmak için makemigrations
# bunlaraı migrate ederek aktarsının

# burada shell acip nesne uretip nesne.save() diyerek elle kayıt ekleyebilriz


# imagefield upload klosoru altına bize parametrede verilen kolsore gorselleri kaydeder
# imageField kullanman için pip install Pillow indirmelisin
class Blog (models.Model):
    # id otomatik veriliyor
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = "blogs")
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    description = models.TextField(null=True)

    # slug olusutrucaz slug bizim categorilerizimiz detaylarını
    # daha iyi olusturmamaıza yarayacak
    # basta ayar icin ture yaptıgımız null ı false layalım
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)

    # bizim ekstra her biri icin slug girmemize gerek yok
    # save metonunu overwrite edip title koyduk mu slug da koymaya ayarlayacagız

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



    # panelimizde veriler basta ne diye gozuksun onun ayarı
    # biz title yaptık
    def __str__(self) -> str:
        return f"{self.title}"
    


class Category (models.Model):
    name = models.CharField(max_length=150)

    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True)
    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    # panelimizde veriler basta ne diye gozuksun onun ayarı
    # biz title yaptık
    def __str__(self) -> str:
        return f"{self.name}"
