import numpy as np

numeros_pares = 0
numeros_impares = 0

while True:
    entrada = np.array(eval(input()))
    
    if np.size(entrada) == 1:
        break
    
    for i in entrada:
        if i % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
    
    print(numeros_pares)
    print(numeros_impares)
    print(np.size(entrada))
    
    numeros_pares = 0
    numeros_impares = 0