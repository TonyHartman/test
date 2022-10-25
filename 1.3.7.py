import pandas as pd
'''
наибольшая сумма балов которую набрал только один абитуриент 
'''
f = pd.read_csv('use.csv')
f["Сумма"] = f["Математика"] + f["Физика"] + f["Русский язык"]
ans = f.groupby(["Сумма"]).size()[f.groupby(["Сумма"]).size() == 1].index.max()
print(ans)