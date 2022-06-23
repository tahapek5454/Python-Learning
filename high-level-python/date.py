

from datetime import date, datetime, timedelta

print(datetime.now()) 
# anlik saat ve tarihi verir

# simdi = datetime.now()

# print(simdi.year)
# print(simdi.hour)

# daha aciklayici bilgi icn

result = datetime.ctime(datetime.now())

print(result)


simdi = datetime.now()

result = datetime.strftime(simdi,"%Y") # direkt parametre de verebiliriz
print(result)

result = datetime.strftime(simdi,"%X") # direkt parametre de verebiliriz
print(result)


# stringden bilgileri ayirma

t = "15 April 2019 hour 10:12:30"

result = datetime.strptime(t,"%d %B %Y hour %H:%M:%S")

print(result)

print(result.day)

# kendimiz bir tarih bilgissi verebilirzz

birthday = datetime(2002,8,9)
print(birthday)

result = datetime.timestamp(birthday) # saniyeye cevrildi
print(result) 

result = datetime.fromtimestamp(result) # saniye to  datetime

print(result)

# iki tarih arasi bilgiyi 

result = simdi  - birthday # timedelta

print(result)

print(result.days)

result = simdi + timedelta(days=10 , hours=1) # simdiki gune 10 gun 1 saat ekledik

print(result)