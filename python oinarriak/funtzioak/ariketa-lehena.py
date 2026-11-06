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




zenbakia = int(input("zenbaki bat emaidazu"))

bikoitza = zenbakia * 2

aurkitua = False
iteratzailea = zenbakia + 1

while (not aurkitua) and (iteratzailea < bikoitza):

    if lehena_da(iteratzailea):
        aurkitua = True

    iteratzailea += 1

if aurkitua:
    print("Aurkitu dut")
else:
    print("Ez dut aurkitu")