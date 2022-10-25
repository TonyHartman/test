import pandas as pd
'''
количество людей с определённым баллом по математике
'''
f = pd.read_csv('use.csv')
df = f.groupby(["Математика"]).aggregate({"Физика": max, "Русский язык": min})
print(df)