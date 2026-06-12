import numpy as np

medias = np.array(eval(input()))
presenca = np.array(eval(input()))
carga_horaria = int(input())

limite_frequencia = carga_horaria * 0.75

situacoes = np.zeros(3, dtype=int)

for i in range(len(medias)):
    if presenca[i] < limite_frequencia:
        situacoes[2] += 1
    else:
        if medias[i] >= 5:
            situacoes[0] += 1
        else: situacoes[1] += 1

print(situacoes)
        
        
