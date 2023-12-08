
nums = []

with open("data.txt", 'r') as file:
    for line in file:
        first_digit = None
        last_digit = None

        for char in line:
            if char.isdigit():
                if first_digit == None:
                    first_digit = char
                last_digit = char
        nums.append(int(first_digit)*10 + int(last_digit))

print(sum(nums))
