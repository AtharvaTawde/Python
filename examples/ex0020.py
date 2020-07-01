lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)

cNum = int(input('Enter a number to check to see if it is in the list shown above: '))

def checkNum():
    if cNum not in lst:
        print('False.', cNum, 'is not in the list shown above.')
    else:
        print('True.', cNum, 'is in the list shown above.')

checkNum()