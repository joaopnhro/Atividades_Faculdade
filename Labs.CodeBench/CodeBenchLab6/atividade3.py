import numpy as np

vet = np.array(eval(input().strip(",")))
acum = 0

for i in range(len(vet)):
    if vet[i] > vet[0] + (vet[0] * 0.2) and vet[i] < vet[0] + (vet[0] * 0.5):
        print(i)
        acum += 1
        
print(acum)