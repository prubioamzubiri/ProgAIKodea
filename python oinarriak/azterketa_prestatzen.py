

loteria_zenbakia = 28756

zenbaki_irabazlea = 48358

zenbaki_asmatuak = 0

while loteria_zenbakia > 0:
    if loteria_zenbakia % 10 == zenbaki_irabazlea %10:
        zenbaki_asmatuak = zenbaki_asmatuak + 1

    loteria_zenbakia = loteria_zenbakia // 10
    #                   28756  --> 2875
    # loteria_zenbakia = 2875
    zenbaki_irabazlea = zenbaki_irabazlea // 10

print(zenbaki_asmatuak)



loteria_zenbakia = 2875

print(loteria_zenbakia%10)

print(loteria_zenbakia // 10)
print(int(loteria_zenbakia / 10))


zenbakia = "123"
print(type(zenbakia))
kopurua = 0

try:
    int(zenbakia)
    kopurua = kopurua + 1
except:
    pass


1 + 1 #2
"asadfsd" == "adfsafas" # False

    