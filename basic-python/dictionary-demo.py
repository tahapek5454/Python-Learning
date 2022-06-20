# kullanıcıdan gelen bilgilerle ogrenci dic olustur


ogrenciler = {}

ogrenci_no = int(input('Ognreci numarainizi giriniz : '))
ogrenci_ad = input("Adinizi giriniz : ")
ogrenci_soyAd = input('Soyadinizi giriniz :')

# ogrenciler[ogrenci_no]={
#     'Ad' : ogrenci_ad,                 # uzun yontem
#     'SoyAd' : ogrenci_soyAd
# }


ogrenciler.update({ogrenci_no : {

            'Ad':ogrenci_ad,
            'SoyAd' : ogrenci_soyAd

}
})

print(ogrenciler)

numara = int(input("Aramak istediginiz ogrencinin numaraisini giriniz : "))

ogrenci = ogrenciler[numara]

print(f"numarali {numara} ogrencinin adi {ogrenci['Ad']}")