import numpy as np

turmas = np.array(eval(input()))
numero_pares = 0
indice_pares = np.array([], dtype=int)
for i in turmas:
    if i % 2 == 0:
        numero_pares += 1

for j in range(len(turmas)):
    if turmas[j] % 2 == 0:
        indice_pares = np.append(indice_pares, j)
        
print(numero_pares)
print(indice_pares)