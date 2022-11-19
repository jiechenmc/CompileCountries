import pandas as pd

df = pd.read_csv("result.tsv", delimiter="\t")

df.to_excel("sheet.xlsx")
