while True:
    word = input('Enter string: ')
    letters = []

    for letter in word:
        letters.append(letter)

    if letters == letters[::-1]:
        print('This word is a palindrome.')
    else:
        print('This word is not a palindrome.')
