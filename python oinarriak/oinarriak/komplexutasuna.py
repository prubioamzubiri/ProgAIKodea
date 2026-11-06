zerrenda = [2, 4, 5,6, 0, 32, 12, 75, 97, 8, 43, 23]

zenbakia = zerrenda[0]
for i in zerrenda:
    if zenbakia < i:
        zenbakia = i

print(zenbakia)

def errepikaturik(zerrenda):
    for i in range(len(zerrenda)):
        for j in range(i+1, len(zerrenda)):
            if zerrenda[i] == zerrenda[j]:
                return True
    return False

print(errepikaturik(zerrenda))

big_array = [2, 4, 5, 6, 0, 32, 12, 75, 97, 8, 43, 23, 7, 8, 13]
sorted_array = sorted(big_array)

def bilaketa_bitarra(zerrenda, bilatua):

    hasiera, bukaera =0, len(zerrenda) - 1

    while hasiera <= bukaera:

        erdikoa = (hasiera + bukaera) // 2
        print (erdikoa)

        if zerrenda[erdikoa] == bilatua:
            return True
        elif zerrenda[erdikoa] < bilatua:
            hasiera = erdikoa + 1
        else:
            bukaera = erdikoa - 1
    
    return False

print(sorted_array)

print(bilaketa_bitarra(sorted_array, 7))


