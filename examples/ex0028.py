x = 3
lst = []
while x > 0:
    y = int(input('Enter number: '))
    lst.append(y)
    x -= 1

lst.sort()
print('The largest number in your list is', str(lst[-1]) + '.')