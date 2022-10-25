import pandas as pd
'''
количество людей с определённым баллом по математике
'''
f = pd.read_csv('use.csv')
print(f.groupby(["Математика"]).size())