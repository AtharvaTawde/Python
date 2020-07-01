gameboard = [(['#'] * 3) for i in range(3)]

row_col = []
turn = 1

def validity(values):
    if len(values) != 2:
        print("Input must be two numbers in format row,col e.g.  1,2\n ")
        return 0
    try:
        if (1 <= int(values[0]) <= 3) and (1 <= int(values[1]) <= 3):
            if gameboard[int(values[0]) - 1][int(values[1]) - 1] != '#':
                print("Position on board already taken.\n")
                return 0
            return 1
        else:
            print("Input values must be numbers between 1 and 3 (inclusive)\n")
            return 0
    except ValueError:
        print("Input values must be numbers between 1 and 3 (inclusive)\n")
        return 0

def drawBoard(values, player):
    gameboard[int(values[0]) - 1][int(values[1]) - 1] = player

    for row in gameboard:
    	print(row)

def gameOver():
    search = '#'
    
    for i in range(3):
        if len(set(gameboard[i])) == 1:
            if gameboard[i][1] == '#':
                continue
            elif gameboard[i][1] == 'X':
                print("Game Over: Player 1 Wins\n")
            else:
                print("Game Over: Player 2 Wins\n")
            return 1

    for i in range(3):
        if gameboard[0][i] == gameboard[1][i] == gameboard[2][i]:
            if gameboard[0][i] == '#':
                continue
            elif gameboard[0][i] == 'X':
                print("Game Over: Player 1 Wins\n")
            else:
                print("Game Over - Player 2 Wins\n")
            return 1

    if (gameboard[0][0] == gameboard[1][1] == gameboard[2][2]) or (gameboard[0][2] == gameboard[1][1] == gameboard[2][0]): 
        if gameboard[1][1] == 'X':
            print("Game Over: Player 1 Wins\n")
        elif gameboard[1][1] == 'O':
            print("Game Over: Player 2 Wins\n")
        else:
            return 0
        return 1

    for sub in gameboard:
        if search in sub:
            return 0

    print("Game Over: The Board Is Full\n")
    return 1

while not gameOver():
    piece = '#'

    while not validity(row_col):
        player = turn % 2
        if player == 0:
            player = 2
            piece = 'O'
        else:
            piece = 'X'
        player = str(player)
        p1 = input('Player ' + str(player) + ' input:\n')
        row_col = p1.split(",")

    drawBoard(row_col, piece)

    row_col = [0]
    turn += 1