'''
Напишите функцию принимающую на вход матрицу содержащую
коэффициенты СЛУ и свободный столбец, и возвращающую решение СЛУ
'''
import numpy as np

def SLE(matrix1, column):
    return(np.linalg.solve(matrix1, column))
