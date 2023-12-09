
output = 0
with open("data.txt", 'r') as file:
    for line in file:
        vals = line.strip().split(" ")
        vals = [int(val) for val in vals]

        lists = [vals]
        
        while True:
            nval = []
            for index in range(len(lists[-1][:-1])):
                curr, next = lists[-1][index], lists[-1][index+1]
                nval.append(next - curr)
            lists.append(nval)
            if sum(nval) == 0:
                break
        
        lists = lists[::-1]
        val = 0

        for list in lists:
            val += list[-1]

        output += val
    

print(output)