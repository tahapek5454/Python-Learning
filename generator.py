
# bellekte yer isgal etmeyen bir iterator olusturur



def cube():

    for i in range(5):
        yield i ** 3

# yield bize bellekten bir alan tahsis etmez direkt degeri bastriri ve geri donusu olmaz
# bize genarotr yollar bu da bir iterabledır yani for dongusu uzerinde rahatca
# bilgileri gorebilirz.

for i in cube():
    print(i)


# su sekilde de tanımlanabilir

genarator = (i**2 for i in range(3))

for i in genarator:
    print(i)
