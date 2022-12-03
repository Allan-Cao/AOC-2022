with open("day1.txt", "r") as f:
    data = f.read().splitlines()
print(data)
max_minions = []
temp = 0
for i in data:
    if i == "":
        max_minions.append(temp)
        temp = 0
    else:
        temp += int(i)

print(sum(sorted(max_minions, reverse=True)[:3]))