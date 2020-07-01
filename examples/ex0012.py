a = [5, 10, 15, 20, 25]
b = []

j = 0
for i in a:
    j += 1

b.append(a[0])
b.append(a[j - 1])

print(b)