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

def check(row, col, num):

    if col > 0:
        if not df.iloc[row, col-1].isdigit() and df.iloc[row, col-1] != '.':
            return True
    if row > 0:
        if not df.iloc[row-1, col].isdigit() and df.iloc[row-1, col] != '.':
            return True
    if col + 1 < df.shape[1]:
        if not df.iloc[row, col+1].isdigit() and df.iloc[row, col+1] != '.':
            return True
    if row + 1 < df.shape[0]:
        if not df.iloc[row+1, col].isdigit() and df.iloc[row+1, col] != '.':
            return True
        

    if row > 0 and col > 0:
        if not df.iloc[row-1, col-1].isdigit() and df.iloc[row-1, col-1] != '.':
            return True
    if row > 0 and col + 1 < df.shape[1]:
        if not df.iloc[row-1, col+1].isdigit() and df.iloc[row-1, col+1] != '.':
            return True
    if row + 1 < df.shape[0] and col + 1 < df.shape[1]:
        if not df.iloc[row+1, col+1].isdigit() and df.iloc[row+1, col+1] != '.':
            return True
    if row + 1 < df.shape[0] and col > 0:
        if not df.iloc[row+1, col-1].isdigit() and df.iloc[row+1, col-1] != '.':
            return True
    
    
    return False
        
        


for row_index in range(df.shape[0]):
    local_num = None
    isGood = False

    for col_index in range(df.shape[1]):
        if df.iloc[row_index, col_index].isdigit():
            digit = int(df.iloc[row_index, col_index])
            if local_num == None:
                local_num = digit
            else:
                local_num *= 10
                local_num += digit
            
            if check(row_index, col_index, local_num):
                isGood = True

        else:
            if local_num and isGood:
                print(f'digit found {local_num}')
                nums.append(local_num)
            local_num = None
            isGood = False

    if local_num and isGood:
        print(f'digit found {local_num}')
        nums.append(local_num)

print(sum(nums))
        
