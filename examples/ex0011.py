while True:    
    number = input('Enter a number: ')
    n = int(number)
    a = []

    x = range(2, n)

    for i in x:
        if n % i == 0:
            a.append(i)

    if a == []:
        print('This number is a prime.')
    else:
        print('This number is a composite.')