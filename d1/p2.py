file = open("input.txt", "r")

nums = [int(line) for line in file]

for line in nums:
    for line2 in nums:
        for line3 in nums:
            if line + line2 + line3 == 2020:
                print(line * line2 * line3)

file.close()