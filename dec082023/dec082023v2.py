steps = None
points_map = dict()
curr_points = []

with open("data.txt", 'r') as file:
    for index, line in enumerate(file):
        if index == 0:
            steps = line
        else:
            split1 = line.strip().split("=")
            from_point = split1[0].strip()
            if from_point[-1] == "A":
                curr_points.append(from_point)


            split2 = split1[1].strip()[1:-1].split(",")
            left_point = split2[0].strip()
            right_point = split2[1].strip()
            points_map[from_point] = [left_point, right_point]

print(steps)
print(points_map)
print(curr_points)
steps = steps.strip()
count = 0
index = 0

zs = []

for curr_point in curr_points:
    count = 0
    while True:
        curr_instr = steps[count % len(steps)]
        if curr_instr == "R":
            curr_point = points_map[curr_point][1]
        else:
            curr_point = points_map[curr_point][0]
        count += 1
        if curr_point[-1] == "Z":
            zs.append(count)
            break

# print(zs)
print(zs)

# first = zs[0]
# second = zs[1]

# for val in first:
#     if val in zs[1] and val in zs[2]:
#         print(val)





# while True:
#     curr_instr = steps[count % len(steps)]
    
#     all_ending = True
#     nlist = []
#     for i, curr_point in enumerate(curr_points):
#         if curr_instr == "R":
#             curr_point = points_map[curr_point][1]
#         else:
#             curr_point = points_map[curr_point][0]
#         curr_points[i] = curr_point
#         if curr_point[-1] != "Z":
#             all_ending = False

#     count += 1
#     print(curr_points, count)

#     if all_ending:
#         break

# print(count)



