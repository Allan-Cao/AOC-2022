stacks = [[],[],[],[],[],[],[],[],[],]
with open("day5.txt", "r") as f:
    while True:
        line = f.readline()
        if line[1] == "1":
            break
        for a in range(int(len(line)/4)):
            value = line[a*4 + 1]
            if value != " ":
                stacks[a].append(value)
    print("---------------------")
    f.readline()
    data = f.read().splitlines()
# Part 1 Logic
# for x in data:
#     amount, start, end = map(int, x.split(" ")[1::2])

#     move = stacks[start-1][:amount]
#     move.reverse()
#     stacks[start-1] = stacks[start-1][amount:]
#     stacks[end-1] = move + stacks[end-1]
# print("".join([stack[0] for stack in stacks]))
# Part 2 Logic
for x in data:
    amount, start, end = map(int, x.split(" ")[1::2])

    move = stacks[start-1][:amount]
    move
    stacks[start-1] = stacks[start-1][amount:]
    stacks[end-1] = move + stacks[end-1]
print("".join([stack[0] for stack in stacks]))