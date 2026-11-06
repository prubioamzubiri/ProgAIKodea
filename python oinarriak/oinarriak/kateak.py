testua = "   Kaixo   Mundua!   "

print(testua.strip())
print(testua.upper())
print(testua.lower())

izena = "pablo rubio"

print(izena.capitalize())
print(izena.title())

def esaldia_refactorizatu(esaldia):
    return esaldia.capitalize()


print(esaldia_refactorizatu("adlfiSAFK saFJEas sdfa."))


testua = "Kaixo Pablo Rubio naiz"

if "naiz" in testua:
    print("naiz testuan dago")
else:
    print("naiz testuan ez dago")

print(testua[0])
print(testua[4])
print(testua[-1])

print(testua.find("Pablo"))
print(testua.count('a'))
print(testua.replace("Kaixo", "Egun on"))


hizkuntzak = "Gaztelania, Euskera, Ingelesa, Frantsesa"
hizkuntzen_zerrenda = hizkuntzak.split(", ") 

print(hizkuntzak)
print(hizkuntzen_zerrenda)

hizkuntzak_gidoituak = ", ".join(hizkuntzen_zerrenda)
print(hizkuntzak_gidoituak)

fitxategia = "python_datuak.csv"

print(fitxategia.startswith("python_"))
print(fitxategia.endswith(".csv"))

karakterea = hizkuntzak[0]
print(karakterea)
print("a" <= karakterea and karakterea <= "z")
print("A" <= karakterea and karakterea <= "Z")

import re

testua = "Nire posta da ane@adibidea.eus"

anonimoa = re.sub(r"\w+@\w+\.\w+", "******@***.***", testua)
#\w+ (testua)
# @
#\w+ (testua)
#\.
#\w+ (testua)
print(anonimoa)
# Nire posta da [EMAIL EZKUTATUTA]


##1
testua = input("testu bat idatzi").strip()
#testua = input("testu bat idatzi")
#testua = testua.strip()
print(testua)

##2
print(testua.upper())
print(testua.lower())

##3
hitzen_zerrenda = testua.split(" ")
print(len(hitzen_zerrenda))

##4
print("_".join(hitzen_zerrenda))



##1

testua = "3 Sagar, 12 plantano eta 7 Banana erosi behar ditut"
zenbakiak = re.findall(r"\d+", testua)
print(zenbakiak)

guztira = 0
for zenbakia in zenbakiak:
    guztira += int(zenbakia)

print(f"guztira: {guztira}")

##2

testua = "kontzertua 2025ean izan zen"
emaitza = re.search(r"\d{4}", testua)
print(emaitza.group())

##3

testua = "3 Sagar, 12 plantano eta 7 Banana erosi behar ditut"
anom = re.sub(r"\d+", "[Zenbakia]", testua)
print(anom)


##1

testua = "3 Sagar, 12 plantano eta 7 Banana erosi behar ditut"
fruta_kopurua = re.findall(r"\d+", testua)

gehiketa = 0
for fruta in fruta_kopurua:
    gehiketa += int(fruta) # string -> int eta gero gehitu

print(f"Guztira {gehiketa} fruta erosi behar ditut")


##2

testua = "kontzertua 2025ean izan zen"

urtea = re.search(r"\d{4}", testua)

print(urtea.group())

##3

testua = "3 Sagar, 12 plantano eta 7 Banana erosi behar ditut"

testu_berria = re.sub(r"\d+", "[ZENBAKIA]", testua)

print(testu_berria)



testua = "jkasdfasdfoḱfasdoñf sdkafjlñasd@a.com"

patroia = r"^\w+@\w+.\w+$"

print(re.search(patroia, testua))


matrizea = [[[1,2,3],[4,5,6],[7,5,7]]]

for j in matrizea:
    for k in j:
        for i in k:
            print(i)