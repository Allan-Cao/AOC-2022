with open("day6.txt", "r") as f:
    bruh = f.readline()
    for i in range(len(bruh)-14):
        day = bruh[i:i+14]
        print(day)
        if (len(set(list(day))) == 14):
            print(i+14)
            break