with open("day4.txt", "r") as file:
    data = file.read().splitlines()
total = 0
for line in data:
    player1, player2 = line.split(",")
    lp1, up1 = map(int, player1.split("-"))
    lp2, up2 = map(int, player2.split("-"))

    # Part 1 Logic
    # if (lp1 <= lp2 and up1 >= up2) or (lp1 >= lp2 and up1 <= up2):
    #     total += 1
    # Part 2 logic
    if not (up1 < lp2 or lp1 > up2):
        total += 1
print(total)
