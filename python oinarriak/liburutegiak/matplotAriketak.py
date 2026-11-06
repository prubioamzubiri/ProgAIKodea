import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,200)

plt.plot(x, np.cos(x), label = "Coseno")
plt.plot(x, np.sin(x), label = "Seno")
i=0
while i < 6.25:
    plt.plot(x, np.cos(x + i))
    i += 0.25

plt.show()


plt.figure(figsize = (4,8))
x = np.linspace(0, 20, 50)
y = x ** 2
y2 = x * 10

plt.plot(x, y, "g--^", label="X Karratua")
plt.plot(x,y2, label="X * 10")
plt.title("X Karratua")
plt.xlabel("X")
plt.ylabel("X Karratua")
plt.legend()
plt.grid(True)
plt.show()

x = ["Fable 5.1", "Opus 5.5", "Groq 4,7", "Astra 6", "Sol 6.1"]
y = [5.1, 5.5, 4.7, 6, 6.1]

plt.bar(x,y)
plt.show()

plt.pie(y, labels = x)
plt.show()

notak = np.random.randint(0, 11, 200) # 200 nota zorizko

plt.hist(notak, bins=10, color="orange", edgecolor="black")
plt.show()

azterketa1 = [4, 6, 7, 5, 9, 3, 8]
azterketa2 = [5, 6, 8, 4, 9, 2, 7]

plt.figure(figsize = (4,8))
plt.scatter(azterketa1, azterketa2, color="purple")
plt.title("Bi azterketen arteko erlazioa")
plt.xlabel("1. azterketa")
plt.ylabel("2. azterketa")
plt.show()


x = np.linspace(0, 20, 50)
fig, ax = plt.subplots(1, 2, figsize=(10, 4)) 

ax[0].plot(x,np.sin(x))
ax[1].plot(x,np.cos(x))

plt.tight_layout()
plt.show()
