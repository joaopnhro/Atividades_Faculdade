import numpy as np

x = input().upper().split(",")
vet = np.zeros(5, dtype=int)

for i in x:
    if i == 'P':
        vet[0] += 1
    elif i == 'C':
        vet[1] += 1
    elif i == 'M':
        vet[2] += 1
    elif i == 'V':
        vet[3] += 1
    elif i == 'A':
        vet[4] += 1
    
print(np.max(vet))
print(vet)
