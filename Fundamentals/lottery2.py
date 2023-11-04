# Code for finding the top player and print thier name and the winnings.


import random
# we create a set with 6 random numbers
lottery_numbers = set(random.sample(list(range(22)), 6))

# the list of players
players = [
    {"name": "Rolf", "numbers": {1, 3, 5, 7, 9, 11}},
    {"name": "Charlie", "numbers": {2, 7, 9, 21, 10, 5}},
    {"name": "Anna", "numbers": {13, 14, 15, 16, 17, 18}},
    {"name": "Jen", "numbers": {19, 20, 12, 7, 3, 5}},
]

top_player = players[0]  # we assume the first player is the top player
 
for player in players:  # we go over each player
    matched_numbers = len(player["numbers"].intersection(lottery_numbers))  # we check how many numbers they guessed
    if matched_numbers > len(top_player["numbers"].intersection(lottery_numbers)):  #  and if they gueeesed more than the current top player...
        top_player = player  # this player is the new top player
 
# we find out the winnings
winnings = 100 ** len(top_player["numbers"].intersection(lottery_numbers))
 
print(f"{top_player['name']} won {winnings}.")
