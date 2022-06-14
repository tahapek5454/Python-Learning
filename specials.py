

class Movie():

    def __init__(self, name,imdb) -> None:
        self.name = name
        self.imdb = imdb
    
    def __str__(self) -> str:  # bu aslinda toString metodunu override etmek gibi biz artik
        return "filmin adi {} ve imdb puani {}".format(self.name,self.imdb)
    
    def __del__(self):
        print("silme islemi basarili")
    
    
        
    


m = Movie("film",6)


print(m)

# obje silmek için del metodu kullanilir onu da override edelim



del m

# bu gibi bircok special methods var bunlara __temp__ seklinde override ederiz