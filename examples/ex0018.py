import random
i = 4
j = []

while i > 0:
    n = random.randint(0, 9)
    j.append(str(n))
    i -= 1

if j[0] == '0':
    j[0] = str(n)

a = input('Guess the number (4-digits): ')

def split(a): 
    return [char for char in a]  

b = split(a)

for i in b:
    k = 0
    l = 0
    if b[k] == j[k]:
        l += 1
    k += 1

print("You got", l, 'digit(s) correct.') 