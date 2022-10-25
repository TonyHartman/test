import numpy as np
'''
Напишите функцию принимающую на вход две матрицы (m,n) и
возвращающую результат их уможения в виде матрицы (m,m)
'''
def matrix(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    print(np.matmul(a, b))
