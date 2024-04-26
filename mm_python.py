
# FURG - Introducao a Computacao de Alto Desempenho
# Turma U - 2024-1
# Prof. Vinicius Garcia Pinto
# 
# Este codigo foi obtido de https://zenodo.org/records/3715525 em 2024-04-19
#
# Executar com: python mm_python.py

import sys, random
from time import *

n = 4096                                 ##\lilabel{set_n}

A = [[random.random()
      for row in range(n)]
     for col in range(n)] ##\lilabel{rand(}
B = [[random.random()
      for row in range(n)]
     for col in range(n)] ##\lilabel{rand)}
C = [[0 for row in range(n)]
     for col in range(n)] ##\lilabel{zero_C}

start = time()                           

for i in range(n):                      ##\lilabel{loop_i}\lilabel{loops(}
    for j in range(n):                  ##\lilabel{loop_j}
        for k in range(n):              ##\lilabel{loop_k}
            C[i][j] += A[i][k] * B[k][j] ##\lilabel{multiply}\lilabel{loops)}

end = time()

print ('%0.6f' % (end - start))
