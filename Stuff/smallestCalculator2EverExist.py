import math

while True:
    try:
        answer = eval(input('Enter an expression to solve (ex: 1 + 2, 3 * 4, etc.): '))
        print('Answer:', round(answer, 3), '\n')
    except:
        print('You have entered an invalid operation. Try again.\n')

print('Literally just 10 lines of code; can you believe it? No imported modules (besides math), no external files, no nothing.')