#tirar a letra a de todas as string inputadas
import numpy as np

s = input()
vet = np.array(list(s))
resultado = []
for i in vet:
    if i != 'a' and i != 'A':
      resultado.append(i)  

resultado_string = "".join(resultado)

print(resultado_string)