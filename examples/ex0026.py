game = [[0, 1, 0],
	    [2, 1, 0],
	    [2, 1, 1]]

i = 0
while True:
    if (game[i][0] == game[i][1] == game[i][2]):
        print('Player', game[i][0], 'has won!')
        break
    elif (game[0][i] == game[1][i] == game[2][i]):
        print('Player', game[0][i], 'has won!')
        break
    elif (game[0][0] == game[1][1] == game[2][2]):
        print('Player', game[0][0], 'has won!')
        break
    elif (game[0][2] == game[1][1] == game[2][0]):
        print('Player', game[0][2], 'has won!')
        break
    else:
        print('You tied!')
        break
    i += 1