import pandas as pd

data = []

with open("data.txt", 'r') as file:
    for line in file:
        valid = True
        cdata = line.strip().split(':')[1]
        print(cdata)
        turns = cdata.strip().split(";")
        color_map = {"red": 0, "blue": 0, "green":0}
        for turn in turns:
            colorCounts = turn.strip().split(",")
            red = 0
            blue = 0
            green = 0

            for colorCount in colorCounts:
                count = int(colorCount.strip().split(" ")[0])
                color = colorCount.strip().split(" ")[1]
                if color == "red":
                    red = count
                elif color == "blue":
                    blue = count
                else:
                    green = count
        
            color_map["red"] = max(color_map["red"], red)
            color_map["blue"] = max(color_map["blue"], blue)
            color_map["green"] = max(color_map["green"], green)
        print(color_map)
        
        val = None
        red = color_map["red"]
        blue = color_map["blue"]
        green = color_map["green"]
        val =  red * blue * green
        data.append(val)

            
print(sum(data))