print("Demagun  ekuazio hau daukagula ax² + bx + c = 0")
a = int(input("emaidazu a"))
b = int(input("emaidazu b"))
c = int(input("emaidazu c"))

balioa = b**2 - 4*a*c

if balioa > 0:
    print("2 emaitza ditu")
elif balioa == 0:
    print("emaitza bakarra du")
else:
    print("ez du emaitzik")


