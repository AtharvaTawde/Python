import sys

for i in range(len(sys.argv)):
    if i == 0:
        print("Current file path: %s" % sys.argv[0])
    else:
        print("%d. argument: %s" % (i, sys.argv[i]))

print('#' * 100)

