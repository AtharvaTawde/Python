import time
import random
name = raw_input("What is your name? ")
print "Hello, " + name + ". Time to play HANGMAN!"
print ''
words = ['physics','apartment','customer','appointment','disease',
         'meat','activity','dinner','guest','director',
         'association','nature','region','article','agreement',
         'instruction','employment','resource','mixture','estate',
         'industry','assumption','payment','analyst','session',
         'lady','tea','courage','map','stupid',
         'scene','vest','face','judge','ink',
         'park','snake','punishment','transport','driving',
         'volleyball','temper','treatment','collar','attraction',
         'boats','farmer','ball','weight','poison',
         'earthy','literate','average','defiant','befitting',
         'teenytiny','gigantic','next','defective','tired',
         'roll','uproot','omit','pull','vary',
         'welcome','treat','lean','express','click'] # dont look at the words list!
n = random.randint(0, len(words) - 1)
guesses = ''
turns = 10
random.shuffle(words)
word = words[n]

print "Choosing secret word..."
time.sleep(3)
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print char,
        else:
            print "_",
            failed += 1
    if failed == 0:
        print "You won"
        break
    guess = raw_input("Guess a letter:")
    guesses += guess
    turns -= 1
    if guess not in word:
        print 'Wrong!'
    print "You have", + turns, 'more guesses'
    if turns == 0:
        print "You Lose. The word was " + word + '.'
    print '\n#################################################################################'