class Ibilgailua:

    def __init__(self, marka, abiadura):
        self.marka = marka
        self.abiadura = abiadura

    def informazioa(self):
        return f"{self.marka} ibilgailua, {self.abiadura}ra iristen da"

class Autoa(Ibilgailua):
    def __init__(self, marka, abiadura, ateak = 5):
        super().__init__(marka, abiadura)
        self.ateak = ateak


auto1 = Autoa("Toyota Corola", 160, 4)

print(auto1.informazioa())

print(isinstance(auto1, Autoa)) # True
print(isinstance(auto1, Ibilgailua)) 


class Pertsona:
    def __init__(self, izena, adina):
        self.izena = izena
        self.adina = adina

    def urtebetetzea(self):
        self.adina += 1


class Ikaslea(Pertsona):
    def __init__(self, izena, adina, ikasgela):
        super().__init__(izena,adina)
        self.ikasgela = ikasgela

    def aurkeztu(self):
        return f"Kaixo {self.izena} naiz, {self.adina} urte ditut eta {self.ikasgela} klasean nago"


class Animalia:
    def __init__(self, izena):
        self.izena = izena
    def soinua_egin(self):
        print(f"{self.izena} soinu bat egiten ari da")

class Txakurra(Animalia):
    def soinua_egin(self):
        print(f"{self.izena}: Wau wau!")

class Katua(Animalia):
    def soinua_egin(self):
        print(f"{self.izena}: Miau Miau!")


def soinua(animalia):
    animalia.soinua_egin()

t = Txakurra("Rex")
k = Katua("Mitxi")
d = Animalia("Mbappe")

soinua(t)
soinua(k)
soinua(d)

class Enpleatua:
    def __init__(self, izena, soldata):
        self.izena = izena
        self.soldata = soldata

    def bonusa_kalkulatu(self):
        return 0

class Zuzendaria(Enpleatua):
    def bonusa_kalkulatu(self):
        return self.soldata * 0.2

class Saltzailea(Enpleatua):
    def bonusa_kalkulatu(self):
        return self.soldata * 0.1

e = Enpleatua("Javier", 1000)
s = Saltzailea("Juan", 1000)
z = Zuzendaria("Pedro", 1000)

print(e.izena, e.bonusa_kalkulatu())
print(s.izena, s.bonusa_kalkulatu())
print(z.izena, z.bonusa_kalkulatu())


x = int(6800/1000)

print(x*1000)
print((x+1)*1000)