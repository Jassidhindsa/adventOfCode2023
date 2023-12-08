
nums = []


def replaceLine(line):
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    arr = [None for _ in range(len(line))]
    for word in words:
        indices = [index for index in range(len(line)) if line.startswith(word, index)]
        for index in indices:
            arr[index] = str(words[word])
    for index,char in enumerate(line):
        if arr[index] == None:
            arr[index] = char
    final_line = ""
    for val in arr:
        if val != None:
            final_line += val
    return final_line



with open("data.txt", 'r') as file:
    for line in file:
        line = replaceLine(line)
        first_digit = None
        last_digit = None

        for char in line:
            if char.isdigit():
                if first_digit == None:
                    first_digit = char
                last_digit = char
        nums.append(int(first_digit)*10 + int(last_digit))

print(sum(nums))
