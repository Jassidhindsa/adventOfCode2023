steps = None
points_map = dict()

with open("data.txt", 'r') as file:
    for index, line in enumerate(file):
        if index == 0:
            steps = line
        else:
            split1 = line.strip().split("=")
            from_point = split1[0].strip()

            split2 = split1[1].strip()[1:-1].split(",")
            left_point = split2[0].strip()
            right_point = split2[1].strip()
            points_map[from_point] = [left_point, right_point]

print(steps)
print(points_map)
steps = steps.strip()
curr_point = "AAA"
count = 0
index = 0

while True:
    curr_instr = steps[index % len(steps)]
    print(curr_instr, curr_point, curr_point in points_map)
    index += 1

    if curr_instr == "R":
        curr_point = points_map[curr_point][1]
    else:
        curr_point = points_map[curr_point][0]
    count += 1
    print(f'currpoint {curr_point}')
    if curr_point == "ZZZ":
        break

print(count)



