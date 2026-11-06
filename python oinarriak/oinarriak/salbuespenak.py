balio_du = False

while not balio_du:

    try:
        #zenbakia = input("Emaidazu zenbaki bat")
        zenbakia = "3"
        zenbakia = int(zenbakia)
        print(f"zenbakia {zenbakia} da, eta hurrengoa {zenbakia + 1} da")
        balio_du = True

    except ValueError:
        print("Idatzitakoa ez da zenbaki bat")

import os
import urllib.request

try:
    with open("quijote_1.txt","r") as fitxategia:
        print(fitxategia.read())

except FileNotFoundError:
    print("fitxategia ez aurkitua, Descargatzen")
    url = ("https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt")
    urllib.request.urlretrieve(url, "quijote_1.txt")


try:
    zatikia = 7
    zatitzailea = 0
    print(zatikia / zatitzailea)
except Exception as e:
    print(f"Errore mota: {type(e).__name__}, mezua: {e}")

def egiaztatu_adina(adina):
    if adina < 0:
        raise ValueError("Adinak ezin du negatiboa izan")
    return adina

try:
    egiaztatu_adina(-5)
except ValueError as e:
    print("Errorea harrapatuta:", e)

try:
    zatitzailea = int(input("zatitzailea: "))
    zatikia = int(input("Zatikia: "))
    emaitza = zatitzailea/zatikia
except ValueError:
    print("Zenbaki osoak izan behar dira")
except ZeroDivisionError:
    print("Zatitzailea ezin du 0 izan")


def nota_ondo(nota):
    if (nota < 0) or (nota > 10):
        raise ValueError("Nota ez dago 0 eta 10 artean")

try:
    nota_ondo(5)
    nota_ondo(-1)
except Exception as e:
    print(f"Errore mota: {type(e).__name__}, mezua: {e}")   









