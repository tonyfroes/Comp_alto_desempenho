# FURG - Introducao a Computacao de Alto Desempenho
# Turma U - 2024-1
# Prof. Vinicius Garcia Pinto
# 
# Este codigo foi obtido de https://zenodo.org/records/3715525 em 2024-04-19
#
# Executar com: python mm_python.py

import sys, random
from time import *
import numpy as np
from numba import cuda

@cuda.jit
def matrix_mult(A, B, C):
    i, j, k = cuda.grid(3)
    if i < C.shape[0] and j < C.shape[1] and k < A.shape[1]:
        C[i][j] += A[i][k] * B[k][j]

n = 4096                                 ##\lilabel{set_n}

A = np.random.rand(n, n)
B = np.random.rand(n, n)
C = np.zeros((n, n))

threadsperblock = (16, 16)
blockspergrid_x = int(np.ceil(A.shape[0] / threadsperblock[0]))
blockspergrid_y = int(np.ceil(B.shape[1] / threadsperblock[1]))
blockspergrid = (blockspergrid_x, blockspergrid_y)

start = time()                           

d_A = cuda.to_device(A)
d_B = cuda.to_device(B)
d_C = cuda.to_device(C)

matrix_mult[blockspergrid, threadsperblock](d_A, d_B, d_C)

d_C.copy_to_host(C)

end = time()

print ('%0.6f' % (end - start))
