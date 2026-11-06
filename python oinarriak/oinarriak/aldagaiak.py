izena = "Pablo"
adina = 31
altuera = 1.75
gaixorik = False

print(izena)
print(adina)
print(altuera)
print(gaixorik)

print(type(izena))
print(type(adina))
print(type(altuera))
print(type(gaixorik))


valioa1 = 4
valioa2 = 7
valioa3 = valioa1 + valioa2

valioa3 = valioa3 + 1
valioa3 += 1

print(valioa3)

print("Izena: ", izena, "Adina: ", adina)

print("Izena:", izena)
print("Adina:", adina)


adina_testua = input("Zenbat urte dituzu? ")
adina = int(adina_testua)

print(f"Datorren urtean {adina + 1} urte izango dituzu")




izena = input("Sartu zure izena")
adina = int(input("sartu zure adina"))
gustuko_zenbakia = int(input("Sartu gustuko zenbaki bat"))

print(f"Zure izena {izena} da, 10 urte barru {adina + 10} urte izango dituzu")
print(f"eta zure zenbaki gustukoaren karratua {gustuko_zenbakia ** 2}")