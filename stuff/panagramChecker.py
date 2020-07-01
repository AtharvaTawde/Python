import string

while True:
    bruh = []
    letters = list(string.ascii_lowercase)
    a = input('Enter Message to Check Panagram')
    a = list(a.lower())

    for i in range(len(a)):
        if a[i] in letters:
            bruh.append(a[i])

    if bruh == letters:
        print('Bruh! It\'s a panagram!')     
    else:
        print('Nice try. It\'s not a panagram!')