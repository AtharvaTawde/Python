import string
import random

print('PASSWORD GENERATOR!')
while True:
    def pswd(size):
        try:
            size = int(size)
            chars = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(chars) for x in range(size))
        except:
            print('You have not entered a numerical value for your character count.')

    password = pswd(input('How many characters in your password? '))

    if password == None:
        print('No password generated.')
    else:
        print('Your password:', password)
    
    print('-' * 40)
    print('\n')