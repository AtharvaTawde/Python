count = int(input("Fibonacci numbers to generate: "))
i = 1
if count == 0:
    fib = []
elif count == 1:
    fib = [1]
elif count == 2:
    fib = [1, 1]
elif count > 2:
    fib = [1, 1]
    while i < (count - 1):
        fib.append(fib[i] + fib[i - 1])
        i += 1

for j in fib:
    print(j)
        