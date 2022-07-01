
html_doc = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ilk web sayfam</title>
</head>
<body>
    <h1>
      Python kursu
  </h1>

    <div class = 'Grup1'>

        <h2>
            Metodlar
        </h2>
   <ul>
    
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
            <li>Menu 4</li>
    
        </ul>

    </div>

<div class = 'Grup2'>

        <h2>
            Classlar
        </h2>
    
        <ul>
    
            <li>Menu 1</li>
            <li>Menu 2</li>
            <li>Menu 3</li>
            <li>Menu 4</li>
    
        </ul>

    </div>

    <a href="http://example1.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example2.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example3.com/elsie" class="sister" id="link1">Elsie</a>,
    
    
</body>
</html>


"""



from unittest import result
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,"html.parser")

result = soup.prettify() # karisik olan dokuman konsola duzeltilmis sekilde gelir

result = soup.title #   basligi getirir

result = soup.head # head kismi Gelir

result = soup.body # body kismini getirir

result = soup.title.name # baslik etiketini getirir

result = soup.title.string # basliga yazdigimiz stringi getirir

result = soup.h1 # h1 etiketi bize gelir

result = soup.h2 # h2 den birden fazla onun ilkini getirir

result = soup.h2.string # h2 deki yazilani getirir

result = soup.find_all('h2') # tum h2 leri liste icersinde getirir liste kurallari geceerlidir

result = soup.find_all("div")[1] # bize 1. indextedki divi getirir

result = soup.find_all("div")[1].ul.find_all('li')[2] #boyle bileske istedigini ulasabiliyorsun

result = soup.div.findChildren() # ilk divin cocuklarini getirir

result = soup.div.find_next_sibling() # ilk divden sonraki dive gecer

# linkleri cekmek

result = soup.find_all('a')

for link in result:
    print(link.get('href'))

#print(result)
