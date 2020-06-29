while True:
    start = input('Initial value: ')
    end = input('Final value: ')

    try:
        start = int(start)
        end = int(end)
    except:
        print("Invalid characters entered!")

    if (type(start) and type(end) is int) and start < end:
        for i in range(start, end + 1):
            print(i)
            i += 1
        print('Difference:', abs(end - start))
    print( '--------------------------------------------------------\n')






    