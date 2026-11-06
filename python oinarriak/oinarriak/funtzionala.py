import random

def eragiketa_egin(funtzioa, balorea):
    return funtzioa(balorea)

bikoiztu = lambda x : x * 2
handitu = lambda x : x + 10
txikitu = lambda x : x - 10



ran_len = random.randint(5,20)
array_1 = []

for i in range(ran_len):
    array_1.append(random.randint(0,20))

###################################################
def eragiketa_arrayetan(funtzioa, array):

    for i in range(len(array)):
    #for n in array

        array[i] = funtzioa(array[i])

##################################################

print(array_1)
eragiketa_arrayetan(handitu, array_1)
print(array_1)
eragiketa_arrayetan(txikitu, array_1)
print(array_1)
eragiketa_arrayetan(bikoiztu, array_1)
print(array_1)

def bikoitia(x):
    if x%2==0:
        return True
    else:
        return False

def hamar_handiagoa(x):
    if x > 10:
        return True
    else:
        return False

bikoitia = lambda x : x % 2 == 0
bikoitia = lambda x : True if x % 2 == 0 else False
hamar_handiagoa = lambda x : x > 10
hamar_handiagoa = lambda x : True if x > 10 else False
print(bikoitia(4))

array_1 = []

for i in range(ran_len):
    array_1.append(random.randint(0,20))

def baldintza_funtzioa_array_batean(baldintza_funtzioa, if_funtzioa, else_funtzioa, array):

    for i in range(len(array)):

        if baldintza_funtzioa(array[i]):
            array[i]  = if_funtzioa(array[i])
        else:
            array[i] = else_funtzioa(array[i])

print(array_1)
baldintza_funtzioa_array_batean(bikoitia, handitu, txikitu, array_1)
print(array_1)
baldintza_funtzioa_array_batean(hamar_handiagoa, txikitu, bikoiztu, array_1)
print(array_1)

def return_0(any):
    return 0

#baldintza_funtzioa_array_batean(hamar_handiagoa, return_0, bikoiztu, array_1)

baldintza_funtzioa_array_batean(hamar_handiagoa, lambda x : 0, lambda x : 2 * x, array_1)

print(array_1)



karratua_egin = lambda x : x ** 2

berreketa = karratua_egin(7)

print(berreketa)

for i in range(len(array_1)):
    print(karratua_egin(array_1[i]))
    print(f"{array_1[i] ** 2}")

ikasleak = [("Ane", 7), ("Jon", 5), ("Uxue", 9)]

def nota_atera(ikaslea):
    return ikaslea[1]

print(nota_atera(ikasleak[0]))

nota_atera = lambda ikaslea : ikaslea[1]

print(nota_atera(ikasleak[0]))


ikasleak = ["Jorge Rubio Perez",
            "Pablo Rubio Amondarain", 
            "Juanjo Gutierrez Lerga",
            "Yolanda Mendez DeJuan",
            "Diego Rubio Amondarain"]




izena = "Pablo Rubio Amondarain"

print(izena.split())

print(izena.split()[1])

def abizena_atera(sarrera_izena):
    return sarrera_izena.split()[1]
    

print(abizena_atera(izena))

abizena_atera = lambda izena : izena.split()[1]

ikasle_ordenatuak = sorted(ikasleak, key = lambda izena : (izena.split()[1], izena.split()[2], izena.split()[0]))

ikasleak.sort(key = lambda izena : izena.split()[1], reverse = True)
ikasleak.sort()

print(ikasleak)
print(ikasle_ordenatuak)


zenbakiak = [1, 2, 3, 4]

karratuak = list(map(lambda x: x ** 2, zenbakiak))
print(karratuak)

abizenak = list(map(abizena_atera,ikasleak))
abizenak = list(map(lambda ikaslea : ikaslea.split()[1], ikasleak))

print(abizenak)

zerrenda = [1,2,3,4,5,6,7,8,9,10,11,12]

bikoitiak = list(filter(lambda x : x % 2 == 0, zerrenda))
bikoitiak = list(filter(bikoitia, zerrenda))
print(bikoitiak)

handi = lambda x : x > 6
sei_handiago = list(filter(handi,zerrenda))
print(sei_handiago)


print("Hegoi" > "Pepe")

hegoi_handiagoa = list(filter(lambda izena: izena.split()[0]> "Hegoi",ikasleak))

print(hegoi_handiagoa)


