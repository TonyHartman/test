'''
Напишите функцию принимающую на вход два вектора и возвращающую
угол между ними в градусах Фаренгейта.
'''
import numpy as np

def theta_degree(a: np.ndarray, b: np.ndarray) -> float:
    l1 = np.linalg.norm(a)
    l2 = np.linalg.norm(b)

    cos = (((a * b).sum())/(l1 * l2))
    return np.arccos(cos) * 180/np.pi