import numpy as np
import scipy
from scipy.ndimage import convolve1d
'''
Напишите функцию принимающую на вход массив чисел и целое число n, а
возвращающую массив чисел усреденных по n соседям
Вывод в float чтобы не потерять точность
'''

def mean_filter(array1: np.ndarray, n: int) ->np.ndarray:
    a = np.array(list(map(lambda x: float(x), array1)))
    w = np.array([1/n for i in range(n)])
    return scipy.ndimage.convolve1d(a, w)



