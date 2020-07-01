prime = open('prime.txt', 'r')
happy = open('happy.txt', 'r')
primeLst = []
happyLst = []
commonLst = []

for line in prime:
    line.strip()
    primeLst.append(int(line))

for line in happy:
    line.strip()
    happyLst.append(int(line))

for line in primeLst:
    if line in happyLst:
        commonLst.append(line)

print(commonLst)