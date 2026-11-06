import os
import urllib.request

if not os.path.exists("quijote_1.txt"):
    url = ("https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt")
    urllib.request.urlretrieve(url, "quijote_1.txt")

with open("quijote_1.txt", "r") as fitxategia:
    edukia = fitxategia.read()
    print(edukia)

with open("froga.txt", "r") as fitxategia:
    
    for lerroa in fitxategia:
        print(lerroa.strip())

with open("froga.txt", "r") as fitxategia:
    
    lerroak = fitxategia.readlines()

print(lerroak)


with open("quijote_1.txt", "r") as fitxategia:
    lerroak = fitxategia.readlines()

#for i in range(len(lerroak)):
#    lerroak[i] = lerroak[i].strip()

lerroak = [lerroa.strip() for lerroa in lerroak]

print(lerroak[:4])

with open("quijote_1.txt", "r") as fitxategia:
    lerroak = [lerroa.strip() for lerroa in fitxategia.readlines()]
print(lerroak[:4])


lerroak = []

with open("quijote_1.txt", "r") as fitxategia:

    for lerroa in fitxategia:

        lerroak.append(lerroa.strip())

print(lerroak[:4])


with open("froga.txt", "a") as fitxategia:
    fitxategia.write("kaixo\n")
    fitxategia.write("egun on\n")

ikasgai_fitxategia = "ikasgaiak.txt"

with open(ikasgai_fitxategia, "w") as fitxategia:
    fitxategia.write("Matematika\n")
    fitxategia.write("Fisika\n")
    fitxategia.write("Kimika\n")

with open(ikasgai_fitxategia, "r") as fitxategia:
    print(fitxategia.read())


with open(ikasgai_fitxategia, "r") as fitxategia:
    ikasgaiak = fitxategia.readlines()


with open(ikasgai_fitxategia, "w") as fitxategia:
    
    for i in range(len(ikasgaiak)):
        fitxategia.write(f"{i+1}. {ikasgaiak[i]}")

ikasgaiak = [f"{i+1}. {ikasgaiak[i]}" for i in range(len(ikasgaiak))]

with open(ikasgai_fitxategia, "w") as fitxategia:
    for i in range(len(ikasgaiak)):
        fitxategia.write(ikasgaiak[i])

with open(ikasgai_fitxategia, "a") as fitxategia:
    fitxategia.write(f"{len(ikasgaiak) + 1}. Historia")


import random
import math

def lehena_da(zenbakia):

    if(zenbakia < 2):
        return False

    iteratzailea = 2
    lehena = True

    while lehena and (iteratzailea < math.sqrt(zenbakia)):

        if zenbakia % iteratzailea == 0:
            lehena = False

        iteratzailea += 1

    return lehena


print(random.randint(0,10000))


kontadorea = 0

with open("zenbakiak.txt", "w+") as fitxategia:

    for i in range(1000):
        fitxategia.write(f"{random.randint(0,10000)}\n")

    fitxategia.seek(0)

    for lerroa in fitxategia:

        zenbakia = int(lerroa)

        if lehena_da(zenbakia):
            kontadorea += 1

print(kontadorea)


        

