num3=int(input("Enter the number you want to convert to bin --> "))
def decimalToBinary(n):
    i=0
    binary = [0] * n  # create an array to store binary numbers
    while n > 0 :
        binary[i]=(n%2)
        n=n//2
        i+=1
    #print(binary)
    for i in binary(-1,i,0):
        print(binary[i],rnd='')
        


decimalToBinary(num3)

