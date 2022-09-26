import this
from django.db import models

# Create your models here.

# not : admin paneline gitmede createsuperuser ile user olusturmalısın

# model bizim databaseimizdeki tablolara dek dusuyor

# gecen yaptıgımız views icersindeki data dict ini buraya koyalım
# ve onu veri tabanına baglayalım


# once migratin olusturmak için makemigrations
# bunlaraı migrate ederek aktarsının

# burada shell acip nesne uretip nesne.save() diyerek elle kayıt ekleyebilriz

class Blog (models.Model):
    # id otomatik veriliyor
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    description = models.TextField(null=True)


    # panelimizde veriler basta ne diye gozuksun onun ayarı
    # biz title yaptık
    def __str__(self) -> str:
        return f"{self.title}"
    


class Category (models.Model):
    name = models.CharField(max_length=150)

    # panelimizde veriler basta ne diye gozuksun onun ayarı
    # biz title yaptık
    def __str__(self) -> str:
        return f"{self.name}"
