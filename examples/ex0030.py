import random
#lst = []
#
#with open('sowpods.txt', 'r') as text:
#    lines = text.readlines()
#
#for line in lines:
#    lst.append(line)
#
#x = random.randint(0, len(lines) - 1)
#
#print(lines[x])


with open('sowpods.txt') as f:
	words = list(f)

print('Your random word of the day:', random.choice(words).strip())