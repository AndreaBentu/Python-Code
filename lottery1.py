# Code to find out each players' correct numbers, and printing out the winning numbers and their name.


player1 = {
    'name': 'Ignacio',
    'numbers': {1, 2, 5, 9, 15}
}
player2 = {
    'name': 'Ramona',
    'numbers': {13, 21, 22, 4, 5}
}

lottery_numbers = {13, 21, 22, 5, 8}

players = ['player1', 'player2']

player1_numbers = lottery_numbers.intersection(player1['numbers'])
player2_numbers = lottery_numbers.intersection(player2['numbers'])

print( *player2_numbers, sep = ", ") 

print( player1['name'] + ' has guessed the following numbers ' + str(player1_numbers)[1:-1] + ' and ' + player2['name'] +' has guessed the following numbers ' + str(player2_numbers)[1:-1] +'.')
