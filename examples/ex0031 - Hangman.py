import time
import random
name = input("What is your name? ")
print("Hello, " + name + ". Time to play HANGMAN!\n")

with open('sowpods.txt') as f:
	words = list(f)

guesses = ''
turns = 10
random.shuffle(words)
word = random.choice(words).strip()

print("Choosing secret word...")
time.sleep(3)
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end= " ")
        else:
            print("_", end= " ")
            failed += 1
    if failed == 0:
        print("You won")
        break
    guess = input("Guess a letter: ").upper()
    guesses += guess
    turns -= 1
    if guess not in word:
        print('Wrong!')
    print("You have", + turns, 'more guesses.')
    if turns == 0:
        print("You Lose. The word was " + word + '.')

    print('\n' + '-' * 100)