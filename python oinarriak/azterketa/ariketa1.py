zenbakia = int(input("zenbaki bat eman?"))

aux = zenbakia
aldrebes = 0
print(aux, aldrebes)

while aux > 0:
    azken_zenbakia = aux % 10
    aldrebes = aldrebes * 10 + azken_zenbakia
    aux = aux // 10 # int(aux/10)
    print(aux, aldrebes)

if aldrebes == zenbakia:
    print("Kapikua")
else:
    print("Ez kapikua")