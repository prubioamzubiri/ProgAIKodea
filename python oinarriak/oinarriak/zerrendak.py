ikasgaiak = [
    "Matematikak",
    "Euskera",
    "Lengua",
    "Barbaro",
    "Historia"
]

ikasgaiak.append("Fisika")
ikasgaiak.insert(1, "Tekno")

print(ikasgaiak)

lehengo_ikasgaia = ikasgaiak.pop(0)
print(lehengo_ikasgaia)
print(ikasgaiak)
print(ikasgaiak[-3:])


zenbakiak = [23, 4, 6 , 7 , 11, 3]
print(zenbakiak)

zenbakiak.sort()
print(zenbakiak)

zenbakiak.sort(reverse=True)
print(zenbakiak)

if 12 in zenbakiak:
    print(zenbakiak.index(12))


zerrenda_ariketa_1 = [23, 8, 45, 12, 4, 45, 30]
zerrenda_ariketa_2 = sorted(zerrenda_ariketa_1)

print(zerrenda_ariketa_1)
print(zerrenda_ariketa_2)

print(zerrenda_ariketa_1.count(45))
print(100 in zerrenda_ariketa_1)


bikoitiak_20_arte = [x for x in range(20) if x % 2 == 0]
lehenengo_20_bikoitiak = [2*x for x in range(20)]

print(bikoitiak_20_arte)
print(lehenengo_20_bikoitiak)


hitza = "hasdfsdfsdfasdf"
print(len(hitza))



zerrenda_a_1 = [x ** 3 for x in range(1,21)]
hitzak = ["etxe", "sagar", "eguzki", "sudur","argi"]
zerrenda_a_2 = [hitz for hitz in hitzak if len(hitz) > 4]
zerrenda_a_3 = [x for x in range(1,50) if x % 3 == 0]

print()
print(zerrenda_a_1)
print(zerrenda_a_2)
print(zerrenda_a_3)


hitza = "Kaixo"

print(hitza[-1])
print(len(hitza))


def berreketa(oinarria, berretzailea):

    if berretzailea == 0:
        return 1
    else:
        return oinarria * berreketa(oinarria, berretzailea - 1)

print(berreketa(4,5))

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci (n - 2)


print(fibonacci(130))