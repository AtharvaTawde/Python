import time
import math
from tkinter import *

def splashLauncher():
    def onclick():
       pass

    root = Tk()
    text = Text(root)
    text.insert(INSERT, "Welcome to GeoCalc! (THIS IS JUST A SPLASH LAUNCHER!)\n")
    text.insert(INSERT, " _____            _____       _\n")
    text.insert(INSERT, "|  __ \          /  __ \     | |\n")
    text.insert(INSERT, '| |  \/ ___  ___ | /  \/ __ _| | ___\n')
    text.insert(INSERT, '| | __ / _ \/ _ \| |    / _` | |/ __|\n')
    text.insert(INSERT, '| |_\ \  __/ (_) | \__/\ (_| | | (\n')
    text.insert(INSERT, ' \____/\___|\___/ \____/\__,_|_|\___|___________________________________________\n')
    text.insert(INSERT, '________________________________________________________________________________\n')
    text.insert(INSERT, 'Created by Atharva Tawde :0\n\n')
    text.insert(INSERT, 'Minor Contributor(s): No One :}\n')
    text.insert(INSERT, 'Before using however, note that this software cannot be redistributed for personal profit, but may be distributed for academic use.\n')
    text.insert(INSERT, 'To complete the loading of the application, X out of this tab now!\n')
    text.insert(INSERT, 'Predecessor and successor to Bruh Calc! (It\'s terrible, BTW!)')
    text.pack()

    text.tag_add("yellow", "1.0", "1.19")
    text.tag_add('red', '2.0', '8.1000')
    text.tag_config("yellow", background="yellow", foreground="blue")
    text.tag_config('red', background='red', foreground='white')
    text.config(state=DISABLED)

    #b = Button(root, text='Quit', command=root.quit)
    #b.pack(side=LEFT, padx=5, pady=5)

    root.mainloop()
    print('WELCOME TO GEOMETRY CALC! Currently supports 5 2d shapes and 8 3d shapes!')
    # don't look!

def printLogo():
    print(" _____            _____       _")
    print("|  __ \          /  __ \     | |")
    print("| |  \/ ___  ___ | /  \/ __ _| | ___")
    print("| | __ / _ \/ _ \| |    / _` | |/ __|")
    print("| |_\ \  __/ (_) | \__/\ (_| | | (")
    print(" \____/\___|\___/ \____/\__,_|_|\___|                     By Atharva Tawde :)\n")
    print("\nMinor Contributors: Aaryan Tawde")

def geoCalc():
    
    twoDOptions = [
        'T: Triangle', 'S: Square/Rectangle', 'R: Trapezoid', 
        'P: Pentagon', 'H: Hexagon', 'A: Heptagon', 
        'O: Octagon', "N: Nonagon", 'D: Decagon'
    ]

    threeDOptions = [
        'S: Sphere', 'T: Triangle Pyramid', 'Q: Square Pyramid', 'C: Cone', 
        'Y: Cylinder', 'N: Triangular Prism', 'U: Cuboid', 'P: Pentagonal Prism', 
        'H: Hexagonal Prism', 'O: Octagonal Prism', 'A: Octahedron', 
        'D: Dodecahedron', 'I: Icosahedron', 'R: Torus'
    ]

    secretCode = 'lol Nyert'

    while True:
        z = input('Do you want to open calculator for 2d or 3d shapes? Type 2d or 3d: ')

        if z == secretCode:
            print("\033[0;37;40m GeoCalc\n")
            print("\033[2;37;40m GeoCalc GeoCalc\033[0;37;40m \n")
            print("\033[1;37;40m GeoCalc GeoCalc\033[0;37;40m \n")
            print("\033[3;37;40m GeoCalc GeoCalc\033[0;37;40m \n")
            print("\033[5;37;40m GeoCalc GeoCalc\033[0;37;40m\n")

            print("\033[1;37;40m \033[2;37:40m GeoCalc GeoCalc          GeoCalc GeoCalc                GeoCalc GeoCalc\033[0;37;40m\n")
            print("\033[1;30;40m GeoCalc GeoCalc      \033[0m 1;30;40m            \033[0;30;47m GeoCalc      \033[0m 0;30;47m               \033[0;37;41m GeoCalc      \033[0m 0;37;41m")
            print("\033[1;31;40m GeoCalc GeoCalc     \033[0m 1;31;40m            \033[0;31;47m GeoCalc        \033[0m 0;31;47m               \033[0;37;42m GeoCalc      \033[0m 0;37;42m")
            print("\033[1;32;40m GeoCalc GeoCalc   \033[0m 1;32;40m            \033[0;32;47m GeoCalc      \033[0m 0;32;47m               \033[0;37;43m GeoCalc      \033[0m 0;37;43m")
            print("\033[1;33;40m GeoCalc         \033[0m 1;33;40m            \033[0;33;47m GeoCalc      \033[0m 0;33;47m               \033[0;37;44m GeoCalc      \033[0m 0;37;44m")
            print("\033[1;34;40m GeoCalc GeoCalc    \033[0m 1;34;40m            \033[0;34;47m GeoCalc       \033[0m 0;34;47m               \033[0;37;45m GeoCalc      \033[0m 0;37;45m")
            print("\033[1;35;40m GeoCalc GeoCalc \033[0m 1;35;40m            \033[0;35;47m GeoCalc    \033[0m 0;35;47m               \033[0;37;46m GeoCalc      \033[0m 0;37;46m")
            print("\033[1;36;40m GeoCalc GeoCalc    \033[0m 1;36;40m            \033[0;36;47m GeoCalc       \033[0m 0;36;47m               \033[0;37;47m GeoCalc      \033[0m 0;37;47m")
            print("\033[1;37;40m GeoCalc          \033[0m 1;37;40m            \033[0;37;40m GeoCalc GeoCalc \033[0m 0;37;40m               \033[0;37;48m GeoCalc      \033[0m 0;37;48m")

        if z in '2D2d':
            while True:
                for shape in twoDOptions:
                    print(shape)
                    time.sleep(0.25)

                a = input('Which shape would you like to solve for? Press e to go back to main menu. ')

                if a in 'Tt':
                    while True:
                        print('Input side lengths of a Triangle. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s1 = input('Side length 1: ') 

                        if s1 in 'exitEXIT':
                            break

                        s2 = input('Side length 2: ')
                        s3 = input('Side length 3: ')

                        try:
                            s1 = int(s1)
                            s2 = int(s2)
                            s3 = int(s3)
                            s = (s1 + s2 + s3) / 2
                            AREA = math.sqrt(s * (s - s1) * (s - s2) * (s - s3))
                            PERIM = s * 2
                            print('Area:', round(AREA, 2), 'units²')
                            print('Perimeter:', round(PERIM, 2), 'units')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Ss':
                    while True:
                        print('Input base and height of a Square/Rectangle. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        b = input('Base: ') 

                        if b in 'exitEXIT':
                            break

                        h = input('Height: ')

                        try:
                            b = int(b)
                            h = int(h)
                            AREA = b * h
                            PERIM = 2 * (b + h)
                            print('Area:', round(AREA, 2), 'units²')
                            print('Perimeter:', round(PERIM, 2), 'units')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Rr':
                    while True:
                        print('Input bases and height of a Trapezoid. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        b1 = input('Base 1: ') 

                        if b1 in 'exitEXIT':
                            break
                        
                        b2 = input('Base 2: ')
                        h = input('Height: ')

                        try:
                            b1 = int(b1)
                            b2 = int(b2)
                            h = int(h)
                            AREA = (b1 + b2) / 2 * h
                            PERIM = b1 + b2 + (2 * math.sqrt((((b1 + b2) / 2) ** 2) + (h * h)))
                            print('Area:', round(AREA, 2), 'units²')
                            print('Perimeter:', round(PERIM, 2), 'units')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Pp':
                    while True:
                        print('Input side length of a Pentagon. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 

                        if s in 'exitEXIT':
                            break

                        try:
                            s = int(s)
                            AREA = 0.25 * math.sqrt(5 * (5 + (2 * math.sqrt(5)))) * s * s
                            PERIM = 5 * s
                            print('Area:', round(AREA, 2), 'units²')
                            print('Perimeter:', round(PERIM, 2), 'units')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Hh':
                    while True:
                        print('Input side length of a Hexagon. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 

                        if s in 'exitEXIT':
                            break

                        try:
                            s = int(s)
                            AREA = 3 * math.sqrt(3) * s * s
                            PERIM = 6 * s
                            print('Area:', round(AREA, 2), 'units²')
                            print('Perimeter:', round(PERIM, 2), 'units')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Aa':
                    while True:
                        print('Input side length of a Heptagon. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 

                        if s in 'exitEXIT':
                            break

                        try:
                            s = int(s)
                            hk = 3.633912444
                            AREA = hk * s * s
                            PERIM = 7 * s
                            print('Area:', round(AREA, 2), 'units²')
                            print('Perimeter:', round(PERIM, 2), 'units')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Oo':
                    while True:
                        print('Input side length of a Octagon. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 
                        if s in 'exitEXIT':
                            break
                        try:
                            s = int(s)
                            AREA = 2 * (1 + math.sqrt(2)) * s * s
                            PERIM = 8 * s
                            print('Area:', round(AREA, 2), 'units²')
                            print('Perimeter:', round(PERIM, 2), 'units')
                        except:
                            print("Please re-input your values.")
                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Nn':
                    while True:
                        print('Input side length of a Nonagon. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 
                        if s in 'exitEXIT':
                            break
                        try:
                            s = int(s)
                            nk = 6.181824194
                            AREA = nk * s * s
                            PERIM = 9 * s
                            print('Area:', round(AREA, 2), 'units²')
                            print('Perimeter:', round(PERIM, 2), 'units')
                        except:
                            print("Please re-input your values.")
                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Dd':
                    while True:
                        print('Input side length of a Decagon. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 
                        if s in 'exitEXIT':
                            break
                        try:
                            s = int(s)
                            AREA = 2.5 * s * s * math.sqrt(5 + (2 * math.sqrt(5)))
                            PERIM = 10 * s
                            print('Area:', round(AREA, 2), 'units²')
                            print('Perimeter:', round(PERIM, 2), 'units')
                        except:
                            print("Please re-input your values.")
                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'exitEXIT':
                    break
                    print('-' * 100)
                    print('\n')


                print('-' * 100)
                print('\n')


            print('-' * 100)
            print('\n')

        if z in '3D3d':
            while True:
                for shape in threeDOptions:
                    print(shape)
                    time.sleep(0.25)

                a = input('Which shape would you like to solve for? Press e to go back to main menu. ')

                if a in 'Ss':   
                    while True:
                        print('Input radius of a Sphere. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        r = input('Radius: ') 

                        if r in 'exitEXIT':
                            break

                        try:
                            r = int(r)
                            VOLUME = 4 / 3 * math.pi * r * r * r
                            SA = 4 * math.pi * r * r
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Tt':   
                    while True:
                        print('Input side length and height of a Triangular Pyramid. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side length: ') 

                        if s in 'exitEXIT':
                            break

                        h = input('Height: ')

                        try:
                            s = int(s)
                            h = int(h)
                            b = math.sqrt(3) / 4 * s * s
                            VOLUME = (1 / 3) * s * h
                            SA = b + (3 / 2) * b * h
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Qq':   
                    while True:
                        print('Input side length and height of a Square Pyramid. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side length: ') 

                        if s in 'exitEXIT':
                            break

                        h = input('Height: ')

                        try:
                            s = int(s)
                            h = int(h)

                            VOLUME = (1 / 3) * s * s * h
                            SA = (s * s) + 2 * s * math.sqrt((s * s / 4) + (h * h))
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Cc':   
                    while True:
                        print('Input side length and height of a Cone. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        r = input('Radius: ') 

                        if r in 'exitEXIT':
                            break

                        h = input('Height: ')

                        try:
                            r = int(r)
                            h = int(h)

                            VOLUME = 1 / 3 * math.pi * r * r * h
                            SA = math.pi * r * (r + math.sqrt(h * h + r * r))
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Yy':   
                    while True:
                        print('Input side length and height of a Cylinder. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        r = input('Radius: ') 

                        if r in 'exitEXIT':
                            break

                        h = input('Height: ')

                        try:
                            r = int(r)
                            h = int(h)

                            VOLUME = math.pi * r * r * h
                            SA = 2 * math.pi * r * (h + r)
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Nn':   
                    while True:
                        print('Input side lengths and height of a Triangular Prism. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s1 = input('Side Length 1: ') 

                        if s1 in 'exitEXIT':
                            break

                        s2 = input('Side Length 2: ') 
                        s3 = input('Side Length 3: ')
                        h = input('Height: ')

                        try:
                            s1 = int(s1)
                            s2 = int(s2)
                            s3 = int(s3)
                            h = int(h)
                            s = (s1 + s2 + s3) / 2
                            p = s * 2
                            VOLUME = (0.25 * h) * math.sqrt(-1 * (s1 ** 4) + 2 * ((s1 * s2) ** 2) + 2 * ((s1 * s3) ** 2) - (s2 ** 4) + 2 * ((s2 * s3) ** 2) - (s3 ** 4))
                            SA = (p * h) + 2 * (math.sqrt(s * (s - s1) * (s - s2) * (s - s3)))
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')  


                if a in 'Uu':   
                    while True:
                        print('Input side length and height of a Cuboid. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        l = input('Length: ') 

                        if l in 'exitEXIT':
                            break

                        w = input('Width: ')
                        h = input('Height: ')

                        try:
                            l = int(l)
                            w = int(w)
                            h = int(h)

                            VOLUME = l * w * h
                            SA = 2 * (l * w + l * h + h * w)
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')  


                if a in 'Pp':   
                    while True:
                        print('Input side length and height of a Pentagonal Prism. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 

                        if s in 'exitEXIT':
                            break

                        h = input('Height: ')

                        try:
                            s = int(s)
                            h = int(h)

                            VOLUME = 1 / 4 * math.sqrt(5 * (5 + (2 * math.sqrt(5)))) * s * s * h
                            SA = 5 * s * h + (1 / 2 * math.sqrt(5 * (5 + (2 * math.sqrt(5))))) * s * s
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Hh':   
                    while True:
                        print('Input side length and height of a Hexagonal Prism. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 

                        if s in 'exitEXIT':
                            break

                        h = input('Height: ')

                        try:
                            s = int(s)
                            h = int(h)

                            VOLUME = 3 * math.sqrt(3) / 2 * s * s * h
                            SA = 6 * s * h + (3 * math.sqrt(3)) * s * s
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Oo':   
                    while True:
                        print('Input side length and height of an Octagonal Prism. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 

                        if s in 'exitEXIT':
                            break

                        h = input('Height: ')

                        try:
                            s = int(s)
                            h = int(h)

                            VOLUME = 2 * (1 + math.sqrt(2)) * s * s * h
                            SA = 8 * s * h + (4 * (1 + math.sqrt(2))) * s * s * h
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Aa':   
                    while True:
                        print('Input side length of an Octahedron. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 

                        if s in 'exitEXIT':
                            break

                        try:
                            s = int(s)

                            VOLUME = math.sqrt(2) / 3 * s * s * s
                            SA = 2 * math.sqrt(3) * s * s
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Dd':   
                    while True:
                        print('Input side length of a Dodecahedron. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 

                        if s in 'exitEXIT':
                            break

                        try:
                            s = int(s)

                            VOLUME = (15 + (7 * math.sqrt(5))) / 4 * s * s * s
                            SA = 3 * math.sqrt(25 + 10 * math.sqrt(5)) * s * s
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Ii':   
                    while True:
                        print('Input side length of an Icosahedron. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        s = input('Side Length: ') 

                        if s in 'exitEXIT':
                            break

                        try:
                            s = int(s)

                            VOLUME = (5 * (3 + math.sqrt(5))) / 12 * (s * s * s)
                            SA = 5 * math.sqrt(3) * s * s
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'Rr':   
                    while True:
                        print('Input major and minor radii of a Torus. Type "e" to exit this operation in the first input box and go back to main menu.\n')
                        print('Otherwise you will continue with the same operation for eternity.\n')
                        R = input('Major Radius: ') 

                        if R in 'exitEXIT':
                            break

                        r = input('Minor Radius: ')

                        try:
                            R = int(R)
                            r = int(r)

                            VOLUME = math.pi * r * r * 2 * math.pi * R
                            SA = 2 * math.pi * R * 2 * math.pi * r
                            print('Volume:', round(VOLUME, 2), 'units³')
                            print('Surface Area:', round(SA, 2), 'units²')

                        except:
                            print("Please re-input your values.")

                        print('-' * 100)
                        print('\n')
                    print('-' * 100)
                    print('\n')


                if a in 'exitEXIT':
                    break
                    print('-' * 100)
                    print('\n')

splashLauncher()
printLogo()
time.sleep(1)
geoCalc()
