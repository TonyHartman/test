import pandas as pd
'''
mean_math - средний балл по математике
'''
f = pd.read_csv('use.csv')
#из прошлой задачи знаем, что у всех есть оченки по всем предметам
print(f["Математика"].mean())

