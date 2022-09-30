from distutils.command.upload import upload
from email.policy import default
import this
from unicodedata import category
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


# foreig key gorsun diye üste aldım
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

    # foreig key ekleyecegiz bloglarımıza cünkü clogları categorilerde sınıflayacagiz
    #category = models.ForeignKey(Category, default=3,  on_delete = models.CASCADE)
    # category i sildim çünkü çok a çok ilişki yapıcam bir blog birden fazla kategoride olabilir
    # MODELS CASCADE category silindi mi blogun da silinmesini saglıyor
    #  onun yerine SET_NULL null=True ya da defaul ataarsın atma da kullanabailirsin
    # basta var olan kayıtlara bu kolon eklenicek ve null olsun istemiyoruz heppsi
    # programlamananın altında oldugudan default olarak onun id sini vereyim

    # .çok çoka ilişki çin
    categories = models.ManyToManyField(Category, blank = True) # hangi model icin oldugunu yazıyorsun o kadar

    # bizim ekstra her biri icin slug girmemize gerek yok
    # save metonunu overwrite edip title koyduk mu slug da koymaya ayarlayacagız

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)



    # panelimizde veriler basta ne diye gozuksun onun ayarı
    # biz title yaptık
    def __str__(self) -> str:
        return f"{self.title}"
    


