
gehiketa = 0

while gehiketa < 10:
    sarrera_zenbakia = input("zenbaki bat emaidazu")
    zenbakia = int(sarrera_zenbakia)
    # zenbakia = int(input("zenbaki bat emaidazu"))

    if zenbakia >= 0:
        gehiketa = gehiketa + zenbakia
        #gehiketa += zenbakia
    else:
        print("zenbaki positiboak sartu")

print(gehiketa)


buclea = True

while buclea:
    sarrera_zenbakia = input("zenbaki bat emaidazu")
    zenbakia = int(sarrera_zenbakia)
    # zenbakia = int(input("zenbaki bat emaidazu"))

    if zenbakia >= 10:
        buclea = False

while True:
    break