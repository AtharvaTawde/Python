#!/usr/bin/env python3

import random

board = [0] * 9

def resetBoard():
    for index, i in enumerate(board):
        board[index] = 0

def printBoard():
    counter = 0
    s = ""
    print("|-----|-----|-----|")
    for index, i in enumerate(board):
        s += "|  "
        if(board[index] == 0):
            s += str(index)
        if(board[index] == 1):
            s += "X"
        if(board[index] == 2):
            s += "O"
        s += "  "
        counter += 1
        if(counter == 3):
            s += "|"
            print(s)
            print("|-----|-----|-----|")
            s = ""
            counter = 0

def getPlayers():
    return input("1 or 2 Players?")

def moveSquare(xOro, ai):
    square = 0
    flag = 0
    while(board[square] != 0 or flag == 0):
        if(ai == 0):
            if(xOro == 1):
                square = eval(input("Choose a square to place X: "))
            if(xOro == 2):
                square = eval(input("Choose a square to place O: "))
        if(ai == 1):
            square = random.randint(0, 8)
        flag = 1
    board[square] = xOro
    print("\n\n")

def checkForWin():
    if(board[0] == board[1] and board[1] == board[2] and board[2] != 0):
        return 1
    if(board[3] == board[4] and board[4] == board[5] and board[5] != 0):
        return 1
    if(board[6] == board[7] and board[7] == board[8] and board[8] != 0):
        return 1
    if(board[0] == board[3] and board[3] == board[6] and board[6] != 0):
        return 1
    if(board[1] == board[4] and board[4] == board[7] and board[7] != 0):
        return 1
    if(board[2] == board[5] and board[5] == board[8] and board[8] != 0):
        return 1
    if(board[0] == board[4] and board[4] == board[8] and board[8] != 0):
        return 1
    if(board[2] == board[4] and board[4] == board[6] and board[6] != 0):
        return 1
    for index, i in enumerate(board):
        if(i == 0):
            break
        if(index == 8):
            return 2
    return 0

def gameOver():
    return eval(input("\nPress 0 to play again!"))

random.seed()
quit = 0
while quit == 0:
    players = 0
    win = 0
    while (players != 1 and players != 2):
        players = eval(getPlayers())
    resetBoard()
    game = 0
    while(game == 0):
        printBoard()
        moveSquare(1, 0)
        game = checkForWin()
        if(game > 0):
            win = game
            break
        printBoard()
        if(players == 1):
            moveSquare(2, 1)
        if(players == 2):
            moveSquare(2, 0)
        game = checkForWin()
        if(game > 0):
            win = game + 1
            break
    if(win == 1):
        print("\nX Wins!")
    if(win == 2):
        print("\nO Wins!")
    if(win == 3):
        print("\n The game is a draw!")
    quit = gameOver()
exit()