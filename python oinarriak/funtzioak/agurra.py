def agurra(izena):
    print(f"Kaixo, {izena}")

agurra(7)
agurra("Juan")


def laukizuzenaren_azalera(zabalera, altuera):
    return zabalera * altuera

def aprobatuta_al_dago(nota):
    emaitza = False

    if (nota >= 5):
        emaitza = True
    else:
        emaitza = False

    return emaitza

def aprobatuta_al_dago_2(nota):
    if (nota >= 5):
        return True
    else:
        return False

def aprobatuta_al_dago_3(nota):
    return (nota >= 5)

azalera = laukizuzenaren_azalera(4,5)
print(azalera)
print(aprobatuta_al_dago(6))
print(aprobatuta_al_dago_2(6))
print(aprobatuta_al_dago_3(4))



def nota_baliagarria(nota):

    if nota >= 0 and nota <= 10:
        baliagarria = True
    else:
        baliagarria = False

    return baliagarria

    #return nota >= 0 and nota <= 10

notak = [1, 2, 11, 4, 5, 6, 7, 8, 9, 10]

baliagarriak = True

for nota in notak:
    if not nota_baliagarria(nota):
        baliagarriak = False
        
    
if baliagarriak:
    print("valio dute")
else:
    print("Baten bat, ez du balio")