import pandas as pd


ncolumns = ["dst","from","range"]
df = pd.read_csv("text.txt", sep=" ", names=ncolumns)

output = []

for index,row in df.iterrows():
    d = [row["dst"], row["from"], row["range"]]
    output.append(d)

print(output)