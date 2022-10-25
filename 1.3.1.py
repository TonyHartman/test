import pandas as pd
'''
number_of_students --- количество обучающихся, у которых хотя бы по одному предмету из трёх есть оценка
'''
f = pd.read_csv('use.csv')
print(f[f.isna()].shape[0])
