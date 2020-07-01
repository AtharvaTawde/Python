while True:
    x = input('Enter a number to convert to hexadecimal: ')

    try:
        x = int(x)
        def numberToHex(num):
            numbers = [
                1000, 900, 500, 400,
                100, 90, 50, 40,
                10, 9, 5, 4,
                1
                ]
            numerals = [
                "M", "CM", "D", "CD",
                "C", "XC", "L", "XL",
                "X", "IX", "V", "IV",
                "I"
                ]
            finalNumeral = ''
            i = 0
            while  num > 0:
                for j in range(num // numbers[i]):
                    finalNumeral += numerals[i]
                    num -= numbers[i]
                i += 1
            return finalNumeral

        print(numberToNumeral(x))
        
    except:
        print('Enter a number in, you bot!')