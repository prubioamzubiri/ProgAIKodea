
def bostenbukatu(zenbakia):
#    return zenbakia % 10 == 5
    if zenbakia % 10 == 5:
        return True
    else:
        return False


def bikoiztu(zenbakia):
    return zenbakia * 2

def gehi10(zenbakia):
    return zenbakia + 10


bostenbukatu = lambda x : x % 10 == 5
bikoiztu = lambda x : 2*x
gehi10 = lambda x : x + 10

def array_baldintzatua(array, baldintza, baiezkoa, ezetzkoa):

    for i in range(len(array)):
        if baldintza(array[i]):
            array[i] = baiezkoa(array[i])
        else:
            array[i] = ezetzkoa(array[i])

array = [1,2,3,4,5,6,7,8,9,10,15]
print(array)

array_baldintzatua(array, bostenbukatu, gehi10, bikoiztu)

print(array)
