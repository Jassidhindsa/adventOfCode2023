import pandas as pd

red = 12
green = 13
blue = 14

row = 1
rows = []

with open("data.txt", 'r') as file:
    for line in file:
        valid = True
        cdata = line.strip().split(':')[1]
        print(cdata)
        turns = cdata.strip().split(";")
        for turn in turns:
            colorCounts = turn.strip().split(",")
            color_map = {"red": 0, "blue": 0, "green":0}

            for colorCount in colorCounts:
                count = int(colorCount.strip().split(" ")[0])
                color = colorCount.strip().split(" ")[1]
                color_map[color] += count
            
            if color_map["red"] > red or color_map["blue"] > blue or color_map["green"]> green:
                valid = False
        
        if valid:
            rows.append(row)
        row += 1

            
            # print(color_map)
        # data.append(columns)

# df = pd.DataFrame(data)

# print(df)
print(sum(rows))