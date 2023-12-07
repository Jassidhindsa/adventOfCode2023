import pandas as pd


df = pd.read_csv("data.txt", sep=r'\s*\|\s*', engine='python', header=None, names=["winning", "playing"])
windf = df['winning'].str.split(':', expand=True)[1].str.strip()

windf = windf.str.extractall('(\d+)').unstack().astype(int)
playdf = df["playing"].str.extractall('(\d+)').unstack().astype(int)

win_col_names = []
play_col_names = []

for i in range(windf.shape[1]):
    win_col_names.append(str(i+1))

for i in range(playdf.shape[1]):
    play_col_names.append(str(i+1))

windf.columns = win_col_names
playdf.columns = play_col_names



print(windf)
print("*"*100)
print(playdf)
output = 0

for row_index in range(windf.shape[0]):
    win_set = set()

    for col_index in range(windf.shape[1]):
        win_set.add(windf.iloc[row_index, col_index])


    count = 0

    for col_index in range(playdf.shape[1]):
        if playdf.iloc[row_index, col_index] in win_set:
            if count == 0:
                count = 1
            else:
                count *= 2
    output += count

print(output)

