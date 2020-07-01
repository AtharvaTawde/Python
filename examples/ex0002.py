while True:
    number = input('Enter number: ')

    try:
        n = int(number)
    except:
        print('You have not entered a number.')
        break

    if n % 2 == 0:
        print(n, 'is even!')
    else:
        print(number, 'is odd!')