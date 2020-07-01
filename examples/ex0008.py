print('''Please pick one:
            Rock
            Scissors
            Paper''')

while True:
    game_dict = {
        'rock': 1, 
        'scissors': 2, 
        'paper': 3
    }

    playerA = str(input("Player A: "))
    playerB = str(input("Player B: "))
    a = int(game_dict.get(playerA))
    b = int(game_dict.get(playerB))
    difference = a - b

    if difference in [-1, 2]:
        print('Player A WINS.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('Game Over.')
            break

    elif difference in [-2, 1]:
        print('Player B WINS.')
        if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
            continue
        else:
            print('Game Over.')
            break

    else:
        print('Draw. Please continue.')
        print('')