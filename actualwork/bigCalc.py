import math
print("CALCULATOR v2.0.")
print("New numerical value added!")
print("PI: simply type 'pi' and use the value in an operation!")
print("Currently is not supported by AVERAGES and you cannot ACCURATELY DIVIDE BY PI, and you cannot MULTIPLY PI BY A NUMBER (PI AS mul1).")
print("You can also not use the base (exp1) as pi, as well")
print("Since PI is an imported library's value, it takes long to implement it in our calculator. We are steadily looking for hotfixes.")
print("AVERAGES: Typing 'DONE' into the first query will still result in a TraceBack Error. We are looking for a hotfix.")
print("------------------------------------------------------------------------------------------------------------------------------")

# code kinda secret, don't source-copy!
def bigCalculator():
    for i in range(1): #bruh why
        print('          _____                _____                    _____                    _____                    _____                    _____                    _____')
        print('         /\    \              /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \ ')
        print('        /::\    \            /::\    \                /::\____\                /::\    \                /::\    \                /::\____\                /::\    \ ')
        print('       /::::\    \           \:::\    \              /:::/    /               /::::\    \              /::::\    \              /:::/    /               /::::\    \ ')
        print('      /::::::\    \           \:::\    \            /:::/    /               /::::::\    \            /::::::\    \            /:::/    /               /::::::\    \ ')
        print('     /:::/\:::\    \           \:::\    \          /:::/    /               /:::/\:::\    \          /:::/\:::\    \          /:::/    /               /:::/\:::\    \ ')
        print('    /:::/__\:::\    \           \:::\    \        /:::/____/               /:::/__\:::\    \        /:::/__\:::\    \        /:::/____/               /:::/__\:::\    \ ')
        print('   /::::\   \:::\    \          /::::\    \      /::::\    \              /::::\   \:::\    \      /::::\   \:::\    \       |::|    |               /::::\   \:::\    \ ')
        print('  /::::::\   \:::\    \        /::::::\    \    /::::::\    \   _____    /::::::\   \:::\    \    /::::::\   \:::\    \      |::|    |     _____    /::::::\   \:::\    \ ')
        print(' /:::/\:::\   \:::\    \      /:::/\:::\    \  /:::/\:::\    \ /\    \  /:::/\:::\   \:::\    \  /:::/\:::\   \:::\____\     |::|    |    /\    \  /:::/\:::\   \:::\    \ ')
        print('/:::/  \:::\   \:::\____\    /:::/  \:::\____\/:::/  \:::\    /::\____\/:::/  \:::\   \:::\____\/:::/  \:::\   \:::|    |    |::|    |   /::\____\/:::/  \:::\   \:::\____\ ')
        print('\::/    \:::\  /:::/    /   /:::/    \::/    /\::/    \:::\  /:::/    /\::/    \:::\  /:::/    /\::/   |::::\  /:::|____|    |::|    |  /:::/    /\::/    \:::\  /:::/    /')
        print(' \/____/ \:::\/:::/    /   /:::/    / \/____/  \/____/ \:::\/:::/    /  \/____/ \:::\/:::/    /  \/____|:::::\/:::/    /     |::|    | /:::/    /  \/____/ \:::\/:::/    /')
        print('          \::::::/    /   /:::/    /                    \::::::/    /            \::::::/    /         |:::::::::/    /      |::|____|/:::/    /            \::::::/    /')
        print('           \::::/    /   /:::/    /                      \::::/    /              \::::/    /          |::|\::::/    /       |:::::::::::/    /              \::::/    /')
        print('           /:::/    /    \::/    /                       /:::/    /               /:::/    /           |::| \::/____/        \::::::::::/____/               /:::/    /')
        print('          /:::/    /      \/____/                       /:::/    /               /:::/    /            |::|  ~|               ~~~~~~~~~~                    /:::/    /')
        print('         /:::/    /                                    /:::/    /               /:::/    /             |::|   |                                            /:::/    /')
        print('        /:::/    /                                    /:::/    /               /:::/    /              \::|   |                                           /:::/    /')
        print('        \::/    /                                     \::/    /                \::/    /                \:|   |                                           \::/    /')
        print('         \/____/                                       \/____/                  \/____/                  \|___|                                            \/____/' + '\n')

    while True:
        ask_user = input("What operation would you like to do? (Enter the number corresponding to the operation as shown below.)\n"
                             "1. Addition\n"
                             "2. Subtraction\n"
                             "3. Multiplication\n"
                             "4. Division\n"
                             "5. Exponent/Power\n"
                             "6. Average Calculator\n")

        intaskuser = []
        try:
            intaskuser = int(ask_user)
        except:
            print("The character(s) you entered to select the operation are invalid.")

        if intaskuser == 1:
            add1 = input("First number to add: ")
            add2 = input("Second number to add: ")
            if add1 != 'pi' and add2 != 'pi':
                try:
                    intadd1 = float(add1)
                    intadd2 = float(add2)
                    print("ANSWER: " + str(intadd1 + intadd2))
                except:
                    print("The characters you entered to add are invalid.")
            elif add1 == 'pi' and add2 != 'pi':
                try:
                    intadd1 = float(math.pi)
                    intadd2 = float(add2)
                    print("ANSWER: " + str(intadd1 + intadd2))
                except:
                    print("The characters you entered to add are invalid.")
            elif add2 == 'pi' and add1 != 'pi':
                try:
                    intadd1 = float(math.pi)
                    intadd2 = float(add1)
                    print("ANSWER: " + str(intadd1 + intadd2))
                except:
                    print("The characters you entered to add are invalid.")
            elif (add1 and add2) == 'pi':
                try:
                    intadd1 = float(math.pi)
                    intadd2 = intadd1
                    print("ANSWER: " + str(intadd1 + intadd2))
                except:
                    print("The characters you entered to add are invalid.")
            print("\n------------------------------------------------------------------------------------------------------")

        elif intaskuser == 2:
            sub1 = input("First number to subtract: ")
            sub2 = input("Second number to subtract: ")
            if sub1 != 'pi' and sub2 != 'pi':
                try:
                    intsub1 = float(sub1)
                    intsub2 = float(sub2)
                    print("ANSWER: " + str(intsub1 - intsub2))
                except:
                    print("The characters you entered to subtract are invalid.")
            elif sub1 == 'pi' and sub2 != 'pi':
                try:
                    intsub1 = float(math.pi)
                    intsub2 = float(sub2)
                    print("ANSWER: " + str(intsub1 - intsub2))
                except:
                    print("The characters you entered to subtract are invalid.")
            elif sub2 == 'pi' and sub1 != 'pi':
                try:
                    intsub1 = float(sub1)
                    intsub2 = float(math.pi)
                    print("ANSWER: " + str(intsub1 - intsub2))
                except:
                    print("The characters you entered to subtract are invalid.")
            elif (sub1 and sub2) == 'pi':
                try:
                    intsub1 = float(math.pi)
                    intsub2 = float(math.pi)
                    print("ANSWER: " + str(intsub1 - intsub2))
                except:
                    print("The characters you entered to subtract are invalid.")
            print("\n------------------------------------------------------------------------------------------------------")

        elif intaskuser == 3:
            mul1 = input("First number to multiply: ")
            mul2 = input("Second number to multiply: ")
            if (mul1 and mul2) != 'pi':
                try:
                    intmul1 = float(mul1)
                    intmul2 = float(mul2)
                    print("ANSWER: " + str(intmul1 * intmul2))
                except:
                    print("The characters you entered to multiply are invalid.")
            elif mul1 == 'pi' and mul2 != 'pi':
                try:
                    intmul1 = float(math.pi)
                    intmul2 = float(mul2)
                    print("ANSWER: " + str(intmul1 * intmul2))
                except:
                    print("The characters you entered to multiply are invalid.")
            elif mul2 == 'pi' and mul1 != 'pi':
                try:
                    intmul1 = float(mul1)
                    intmul2 = float(math.pi)
                    print("ANSWER: " + str(intmul1 * intmul2))
                except:
                    print("The characters you entered to multiply are invalid.")
            elif (mul1 and mul2) == 'pi':
                try:
                    intmul1 = float(math.pi)
                    intmul2 = float(math.pi)
                    print("ANSWER: " + str(intmul1 * intmul2))
                except:
                    print("The characters you entered to multiply are invalid.")
            print("\n------------------------------------------------------------------------------------------------------")

        elif intaskuser == 4:
            div1 = input("First number to divide: ")
            div2 = input("Second number to divide: ")
            if (div1 and div2) != 'pi':
                try:
                    intdiv1 = float(div1)
                    intdiv2 = float(div2)
                    print("ANSWER: " + str(intdiv1 / intdiv2))
                except:
                    print("The characters you entered to divide are invalid.")
            elif div1 == 'pi' and div2 != 'pi':
                try:
                    div = float(div2)
                    print("ANSWER: " + str(math.pi / div))
                except:
                    print("The characters you entered to divide are invalid.")
            elif div2 == 'pi' and div1 != 'pi':
                try:
                    div = float(div1)
                    print("ANSWER: " + str(div / math.pi))
                except:
                    print("The characters you entered to divide are invalid.")
            elif (div1 and div2) == 'pi':
                try:
                    div = math.pi
                    print("ANSWER: " + str(div / div))
                except:
                    print("The characters you entered to divide are invalid.")
            print("\n------------------------------------------------------------------------------------------------------")

        elif intaskuser == 5:
            exp1 = input("Base number: ")
            exp2 = input("Exponent: ")
            if (exp1 and exp2) != 'pi':
                try:
                    intexp1 = float(exp1)
                    intexp2 = float(exp2)
                    print("ANSWER: " + str(intexp1 ** intexp2))
                except:
                    print("The characters you entered are invalid.")
            elif exp1 == 'pi' and exp2 != 'pi':
                try:
                    intexp1 = float(math.pi)
                    intexp2 = float(exp2)
                    print("ANSWER: " + str(intexp1 ** intexp2))
                except:
                    print("The characters you entered are invalid.")
            elif exp1 != 'pi' and exp2 == 'pi':
                try:
                    intexp1 = float(exp1)
                    print("ANSWER: " + str(intexp1 ** math.pi))
                except:
                    print("The characters you entered are invalid.")
            elif (exp1 and exp2) == 'pi':
                try:
                    print("ANSWER: " + str(math.pi ** math.pi))
                except:
                    print("The characters you entered are invalid.")
            print("\n------------------------------------------------------------------------------------------------------")

        elif intaskuser == 6:
            j = 0
            k = 0
            print("Type a value and press Enter to enter the next value. Type 'DONE' exactly as shown to break out of the queries and find your average.")
            while True:
                number = input("Enter number: ")

                if number == "DONE":
                    break

                try:
                    floatn = float(number)
                except:
                    print("Invalid input")
                    continue

                j += floatn
                k += 1

            print("Average:", str(j/k))
            print("\n------------------------------------------------------------------------------------------------------")
        else:
            print("Your input is invalid. Try selecting another operation.")
            print("\n------------------------------------------------------------------------------------------------------")

bigCalculator() #run the thingy