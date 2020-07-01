dxt = {}
a = open('ex.txt', 'r')

for line in a:
    while line:
        line = line.strip()
        if line in dxt:
        	dxt[line] += 1
        else:
        	dxt[line] = 1
        line = a.readline()

print(dxt)