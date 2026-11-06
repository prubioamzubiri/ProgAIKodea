import numpy as np

zerrenda_arrunta = [1,2,3,4,5]
zerrenda_numpy = np.array(zerrenda_arrunta)

print(zerrenda_numpy)
print(type(zerrenda_numpy))

print (np.zeros(7))
print (np.ones(10))
print (np.full(8, 14.))

print (np.arange(0,100,5))
print ( np.linspace(0,1,5))

print(np.random.rand(11))
print(np.random.randint(0,11,11))

print (np.arange(0,201,25))
print ( np.linspace(0,200,9))

zerrenda_arrunta = [10, 20, 30, 40, 50]
zerrenda_numpy = np.array(zerrenda_arrunta)
#zerrenda_numpy = np.arange(10,51,10)

sei_zero = np.zeros(6)

bikoitien_zerrenda = np.arange(0,20,2)

np.random.seed(50)

zerrenda_rand = np.random.randint(0,100,10)

print(zerrenda_numpy)
print(sei_zero)
print(bikoitien_zerrenda)
print(zerrenda_rand)

matrizea = np.array([[1,2,3], [2,4,6]])

print(matrizea.ndim)
print(matrizea.shape)
print(matrizea.size)

print(np.linalg.matrix_rank(matrizea))

matrizea = np.array([[1,2], [3,4], [5,6]])

print(matrizea.ndim)
print(matrizea.shape)
print(matrizea.size)

m = np.array([[2,4,6],[8,10,12],[14,16,18]])

print(m[1]) #[8,10,12]
print(m[:,2]) #[6,12,18]
print(m[1,1]) #10
print(m[0:2,0:2]) #[2,4][8,10]

notak = np.array([[7, 6, 8],
                  [5, 9, 7],
                  [8, 8, 6]])

ikasleen_batazbestekoa = notak.mean(axis = 1)
ikasgaien_batazbestekoa = notak.mean (axis = 0)
nota_altuena = notak.max()

print(notak.mean())

print(ikasleen_batazbestekoa)
print(ikasgaien_batazbestekoa)
print(nota_altuena)

notak = np.array([3, 5, 8, 4, 9, 6, 7, 2, 10, 5])

maximoa = notak.max()
minimoa =notak.min()
batazbestekoa =notak.mean()
desbideraketa_tipikoa = notak.std()

print("Maximoa:", maximoa)
print("Minimoa:", minimoa)
print("Batazbestekoa:", batazbestekoa)
print("Desbideraketa tipikoa:", desbideraketa_tipikoa)

suspendituen_maskara = notak < 5

suspendituen_zerrenda = notak[suspendituen_maskara]
print("Suspendituen zerrenda:", suspendituen_zerrenda)
aprob = notak >= 5
print("Aprobatuen kopurua:", aprob.sum())


