file = open("input.txt", "r")

valid_passwords = 0

for line in file:
    validity = 0
    line = line.strip()
    line = line.split(":")
    print(line)
    password = line[1].strip()
    line = line[0].split()
    print(line)
    char = line[1]
    policy = line[0].split("-")
    policy = [int(i) for i in policy]
    print(policy)
    if (password[policy[0] - 1] == char) ^ (password[policy[1] - 1] == char):
        valid_passwords += 1
        
print(valid_passwords)
file.close()