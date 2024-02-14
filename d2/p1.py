file = open("input.txt", "r")

valid_passwords = 0

for line in file:
    line = line.strip()
    print(line)
    line = line.split(":")
    password = line[1]
    line = line[0].split()
    char = line[1]
    policy = line[0].split("-")
    policy = [int(i) for i in policy]
    if password.count(char) < policy[1] and password.count(char) > policy[0]:
        valid_passwords += 1

file.close()