'''
Напишите функцию принимающую на вход генератор целых чисел и
возвращающую новый генератор в котором отфильтровываюся числа делящиеся на
3, а оставшиеся возводятся в квадрат
'''

def generator(list_gen):
    ans = list(map(lambda x: x ** 2, list(filter(lambda x: x % 3 !=0, list_gen))))
    return ans
