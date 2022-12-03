with open("day3.txt", "r") as f:
    data = f.read().splitlines()

def get_priority(char):
    if char.isupper():
        return ord(char)-38
    else:
        return ord(char)-96

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

# print("a", get_priority("a"))
# print("z", get_priority("z"))
# print("A", get_priority("A"))
# print("Z", get_priority("Z"))

total = 0
line = 0
for i in range(int(len(data)/3)):
    line = i*3
    sacks = data[line:line+3]
    for character in sacks[0]:
        print(character, sacks[1], sacks[2], (character in sacks[2]))
        if character in sacks[1] and character in sacks[2]:
            total += get_priority(character)
            break
print(total)