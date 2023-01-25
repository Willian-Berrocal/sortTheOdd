# Este programa recibe una lista de numeros, y devuelve una similar, con la variacion de que sus elementos impares
# estan ordenados.
# La complejidad del programa depende de como implementaron la funcion sorted(), ya que lo demas es O(n), siendo n
# el len de la lista de input

import numpy as np

m = np.array([5, 8, 6, 3, 4, 1])

sortedOdds = sorted(m[m % 2 != 0])
j = 0

for i in range(0, len(m)):
    if m[i] % 2 != 0:
        m[i] = sortedOdds[j]
        j += 1


print(m.tolist())
