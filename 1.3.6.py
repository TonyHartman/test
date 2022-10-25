import pandas as pd
'''
количество студентов с одинаковыми баллами по всем трём предметам
'''
f = pd.read_csv('use.csv')
series = f["Математика"] + f["Физика"] + f["Русский язык"]
print(series)