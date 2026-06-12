import numpy as np

entrada = np.array(eval(input()))
saida = (entrada - 1) % 10

print(saida)