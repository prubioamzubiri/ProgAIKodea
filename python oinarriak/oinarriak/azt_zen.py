import random

with open("zenbakiak.txt", "w") as fitxategia:

    for i in range(1000):
        fitxategia.write(f"{random.randint(0,300)}\n")



#### EZ bazarete gai fitxategia irakurtzeko ###
################################################# 
zenbakiak = []

for i in range(1000):
    zenbakiak.append(random.randint(0,300))
#################################################
