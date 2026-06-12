import numpy as np

quant_livros = np.zeros(4, dtype=int)

livros = input().upper().split(",")

for i in livros:
    if i == "R":
        quant_livros[0] += 1
    elif i == "F":
        quant_livros[1] += 1
    elif i == "S":
        quant_livros[2] += 1
    elif i == "T":
        quant_livros[3] += 1

print(quant_livros)