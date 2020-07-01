rows = int(input('How many rows would you like? '))
columns = int(input('How many columns would you like? '))

h = []
v = []
e = []

for i in range (0, columns):
    v.append('|   |')

for j in range(0, columns):
    e.append(' --- ')

while rows > 0:
    while columns > 0:
        h.append(' --- ')
        columns -= 1
    rows -= 1

    horizontal = ''.join(h)
    vertical = ''.join(v)
    extraline = ''.join(e)
    print(horizontal)
    print(vertical)

print(extraline)