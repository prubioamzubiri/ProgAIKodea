
with open("zenbakiak.txt", "r") as fitxategia:
    zenbakiak = fitxategia.readlines()

zenbakiak = [int(zenbakiak[i]) for i in range(len(zenbakiak))]

for i in range(len(zenbakiak)):
    zenbakiak[i] = int(zenbakiak[i])

print(zenbakiak)

zenbakiak.sort(reverse=True)

#zenbakiak = zenbakiak[::-1]

handiena = zenbakiak[0]
handiena2 = None
kont = 0
zenbaki_kopurua = len(zenbakiak)

while handiena2 == None and kont < zenbaki_kopurua:

    if not zenbakiak[kont] == handiena:
        handiena2 = zenbakiak[kont]

    kont += 1

if not handiena2 == None:
    print(f"zenbaki handienak {handiena} eta {handiena2} dira")
else:
    print(f"Bakarrik zenbaki desberdin bat dago eta {handiena} da")

kont = 0
moda = None
zenbaki_aux = 0
kopurua_moda = 0
kopurua_orain = 0

while kont < zenbaki_kopurua:

    while kont < zenbaki_kopurua and zenbakiak[kont] == zenbaki_aux:
        kopurua_orain += 1
        kont += 1

    if kopurua_orain > kopurua_moda:
        moda = zenbaki_aux
        kopurua_moda = kopurua_orain

    if kont < zenbaki_kopurua:
        zenbaki_aux = zenbakiak[kont]
        kopurua_orain = 1
        kont += 1

print(f"Gehien agertzen den zenbakia {moda} da {kopurua_moda} aldiz")


moda = 0
zenbaki_aux = 0
kopurua_moda = 0
kopurua_orain = 0

for i in range(len(zenbakiak)):

    kopurua_orain = 0

    for j in range(len(zenbakiak)):

        if moda == zenbakiak[j]:
            kopurua_orain += 1

    if kopurua_orain > kopurua_moda:
        moda = zenbakiak[i]
        kopurua_moda = kopurua_orain

