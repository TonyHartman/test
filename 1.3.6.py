import pandas as pd

f = pd.read_csv('use.csv')
series = f["Математика"] + f["Физика"] + f["Русский язык"]
print(series)