import random

m = 50
tries = 10

while tries > 0:
    tries -= 1
    print('Is the guess', str(m) + '? Type H for higher, L for lower, or C for correct')
    a = input('Enter response: ')

    if a == "H":
        x = random.randint(0, 51)
        m += x
        while m > 100:
            m -= 1
        continue
    if a == 'L':
        x = random.randint(0, 51)
        m -= x
        while m < 0:
            m += 1
        continue
    if a == 'C':
        print('I guessed the number correctly!')
        break
        
if tries == 0:
    print("I have failed to guess your number. Oof.")
