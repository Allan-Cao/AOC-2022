win_map = {
    "A": "B",
    "B": "C",
    "C": "A"
}
loss_map = {
    "A": "C",
    "B": "A",
    "C": "B"
}
outcome_map = {
    "X": 0,
    "Y": 3,
    "Z": 6
}
value_map = {
    "A": 1,
    "B": 2,
    "C": 3
}
with open("day2.txt", "r") as f:
    data = f.read().splitlines()

score = 0
# for game in data:
#     game = game.split(" ")
#     print(game)
#     if draw_map[game[1]] == game[0]: # draw = +3
#         score += 3
#     elif win_map[game[1]] == game[0]: # win = +6
#         score += 6
#     score += outcome[game[1]]
# print(score)

for game in data:
    opponent, outcome = game.split(" ")
    
    if outcome_map[outcome] == 3: # if the game is a draw
        score += value_map[opponent]
    elif outcome_map[outcome] == 6: # if the game is a win
        score += value_map[win_map[opponent]]
    else:
        score += value_map[loss_map[opponent]]
    score += outcome_map[outcome]
print(score)