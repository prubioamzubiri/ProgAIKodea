class KontuBankarioa:
    def __init__(self, titularra, saldoa):
        self.titularra = titularra
        self.__saldoa = saldoa # "pribatua" konbentzioz


    @property
    def saldoa(self):
        x = int(self.__saldoa/1000)
        return f"Zure saldoa {x*1000} eta {(x+1)*1000} artean dago."

    @saldoa.setter
    def saldoa(self, saldo_berria):
        if saldo_berria >= 0:
            self.__saldoa = saldo_berria
        else:
            print("Error")

kb = KontuBankarioa("juanjo", 1000)

kb.saldoa = -50
#print(kb.saldoa_ikusi())
kb.saldoa = 2030
#print(kb.saldoa_ikusi())
print(kb.saldoa)
kb.saldoa = 6000
print(kb.saldoa)


class Zirkuloa:

    kopurua = 0

    def __init__(self, radioa):
        self.radioa = radioa
        Zirkuloa.kopurua += 1

    @staticmethod
    def da_erradioa_baliozkoa(erradioa):
        #return erradioa > 0
        if erradioa > 0:
            return True #Erradioa positivoa
        else:
            return False

    @classmethod
    def kopurua_jakin(cls):
        return cls.kopurua

    @property
    def azalera(self):
        return 3.14 * (self.radioa ** 2)

    @property
    def perimetroa(self):
        return 2 * 3.14 * self.radioa


print(Zirkuloa.kopurua_jakin())
zirku1 = Zirkuloa(4)
print(Zirkuloa.kopurua_jakin())

print(zirku1.azalera)
print(zirku1.perimetroa)

    