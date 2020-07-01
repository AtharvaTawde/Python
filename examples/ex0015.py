a = input('Write a string that you want returned backwards: ')

while True:
    if type(a) != str:
        #print('You have not entered a string!')
        break
    
    a = a.split()
    a = a[::-1]

for j in a:
    print(j)