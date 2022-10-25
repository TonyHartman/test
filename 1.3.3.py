import pandas as pd
'''
средний балл физиков по русскому
'''
f = pd.read_csv('use.csv')
print(f[f["Физика"] == 100]["Русский язык"].mean())
