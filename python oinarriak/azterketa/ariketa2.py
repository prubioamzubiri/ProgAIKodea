ikasgaiak = ["Euskera", "Mate", "Lengua"]

#1.aukera
for i in range(len(ikasgaiak)):
    ikasgaiak[i] = f"{i+1}. {ikasgaiak[i]}"

print(ikasgaiak)


#2. aukera

ikasgaiak = ["Euskera", "Mate", "Lengua"]

ikasgaia_berria = []

for i in range(len(ikasgaiak)):
    ikasgaia_berria.append(f"{i+1}. {ikasgaiak[i]}")

print(ikasgaia_berria)

#3. Aukera

ikasgaiak = ["Euskera", "Mate", "Lengua"]

ikasgaiak = [f"{i+1}. {ikasgaiak[i]}" for i in range(len(ikasgaiak))]

print(ikasgaiak)