import pandas as pd


df = pd.read_csv("data.txt", names=["d"])
numdf = df["d"].str.extractall('(\d+)').unstack()
df = df["d"].apply(list)

cols = [f'{i}' for i in range(len(df.iloc[0]))]
df = pd.DataFrame(df.tolist(), columns=cols)



print(df)
print(df.shape)
print(len(df.iloc[0]))
# print(df.loc[0,"col1"])

print(numdf)

nums = []
gears = {}
currGears = set()


for row_index in range(df.shape[0]):
    for col_index in range(df.shape[1]):
        if df.iloc[row_index, col_index] == "*":
            gears[row_index, col_index] = []

print(gears)




def check(row, col, num):

    if col > 0:
        if df.iloc[row, col-1] == "*":
            currGears.add((row, col-1))
    if row > 0:
        if df.iloc[row-1, col] == '*':
            currGears.add((row-1, col))
    if col + 1 < df.shape[1]:
        if df.iloc[row, col+1] == '*':
            currGears.add((row, col+1))
    if row + 1 < df.shape[0]:
        if df.iloc[row+1, col] == '*':
            currGears.add((row+1, col))
        

    if row > 0 and col > 0:
        if df.iloc[row-1, col-1] == '*':
            currGears.add((row-1, col-1))
    if row > 0 and col + 1 < df.shape[1]:
        if df.iloc[row-1, col+1] == '*':
            currGears.add((row-1, col+1))
    if row + 1 < df.shape[0] and col + 1 < df.shape[1]:
        if df.iloc[row+1, col+1] == '*':
            currGears.add((row+1, col+1))
    if row + 1 < df.shape[0] and col > 0:
        if df.iloc[row+1, col-1] == '*':
            currGears.add((row+1, col-1))
    
    
    return
        
        


for row_index in range(df.shape[0]):
    local_num = None
    
    for col_index in range(df.shape[1]):
        if df.iloc[row_index, col_index].isdigit():
            digit = int(df.iloc[row_index, col_index])
            if local_num == None:
                local_num = digit
            else:
                local_num *= 10
                local_num += digit
            
            check(row_index, col_index, local_num)

        else:
            if local_num:
                for gear in list(currGears):
                    print(gear)
                    gears[gear].append(local_num)
                nums.append(local_num)
            local_num = None
            currGears = set()

    if local_num:
        for gear in currGears:
                    gears[gear].append(local_num)
        nums.append(local_num)
        currGears = set()

# print(sum(nums))
print(gears)
output = 0

for gear in gears.keys():
    if len(gears[gear]) == 2:
        val = gears[gear][0] * gears[gear][1]
        output += val

print(output)

        
