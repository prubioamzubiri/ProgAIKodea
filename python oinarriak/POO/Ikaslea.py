class Ikaslea:
    def __init__(self, izena, adina, ikasgela):
        self.izena = izena
        self.adina = adina
        self.ikasgela = ikasgela

    def aurkeztu(self):
        return f"Kaixo {self.izena} naiz, {self.adina} urte ditut eta {self.ikasgela} klasean nago"

    def urtebetetzea(self):
        self.adina += 1

ikasle1 = Ikaslea("Ane", 16, "A")
ikasle2 = Ikaslea("Jon", 17, "B")

print(ikasle1.izena)

if ikasle1.adina > ikasle2.adina:
    print("Lehenego ikaslea adina gehiago dauka")
elif ikasle1.adina == ikasle2.adina:
    print("Adin berdina dute")
else:
    print("Bigarren ikaslea adina gehiago dauka")

class Liburua:

    liburu_kopurua = 0
    liburu_irakurriak = 0

    def __init__(self, izenburua, egilea, urtea, irakurria = False):
        self.izenburua = izenburua
        self.egilea = egilea
        self.urtea = urtea
        #self.irakurria = False
        self.irakurria = irakurria
        Liburua.liburu_kopurua += 1

        if irakurria:
            Liburua.liburu_irakurriak += 1

    def irakurrita_markatu(self):

        if not self.irakurria:
            Liburua.liburu_irakurriak += 1 
            self.irakurria = True
    
    def informazioa(self):
        return f"{self.izenburua} liburua, {self.egilea}k idatzia {self.urtea} urtean eta {self.irakurria} irakurri dut."

print(ikasle1.aurkeztu())
print(ikasle2.aurkeztu())

ikasle1.urtebetetzea()

print(ikasle1.aurkeztu())

class Laukizuzena:
    def __init__(self, altuera, zabalera):
        self.altuera = altuera
        self.zabalera = zabalera

    def azalera(self):
        return self.altuera * self.zabalera

    def perimetroa(self):
        return 2 * (self.altuera + self.zabalera)


liburu1 = Liburua("Harry Potter", "JKR", 1991)
liburu2 = Liburua("El señor de los anillos", "Tolkien", 1954, True)
liburu3 = Liburua("El principito", "Saint-Exupéry", 1943)
liburu4 = Liburua("El alquimista", "Paulo Coelho", 1988, True)
liburu5 = Liburua("El código Da Vinci", "Dan Brown", 2003)
liburu6 = Liburua("El juego de Ender", "Orson Scott Card", 1985, True)

print(liburu1.informazioa())
liburu1.irakurrita_markatu()
print(liburu1.informazioa())

print(Liburua.liburu_kopurua)