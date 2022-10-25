'''
Напишите функцию принимающую на вход массив чисел и два числа `treshold` и `width`,
а возвращающую списком индексы пиков которые превышают `treshold` и вокруг которых
на растоянии `width/2` нет больших пиков.
'''

def find_peak(list1: list, treshold: float, width: float) -> list:
    selection1 = []
    for i in range(len(list1)):
        if list1[i] > treshold:
            selection1.append(i)
    selection2 = []
    if len(selection1) >= 2:
        if selection1[0] + width / 2 < selection1[1]:
            selection2.append(selection1[0])
        for i in range(1, len(selection1) - 1):
            if (selection1[i - 1] < selection1[i] - width/2) and (selection1[i + 1] > selection1[i] + width/2):
                selection2.append(selection1[i])
        if selection1[-1] - width / 2 > selection1[-2]:
            selection2.append(selection1[-1])
    else:
        selection2 = selection1.copy()
    return selection2