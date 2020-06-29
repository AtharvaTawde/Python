from tkinter import *
import time
import math

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
    text.insert(INSERT, 'Minor Contributor(s): Aaryan Tawde :}\n')
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
    while True:
        time.sleep(1.5)
        bruh = input('Would you like to load 2d or 3d calculator? Type 2d or 3d: ')
        print("-" * 100)
        print('\n')
        if bruh == '2d' or bruh == '2D':
            print('T: Triangle')
            time.sleep(0.25)
            print('S: Square/Rectangle')
            time.sleep(0.25)
            print('P: Parallelogram')
            time.sleep(0.25)
            print('Z: Trapezoid')
            time.sleep(0.25)
            print('C: Circle')
            time.sleep(0.25)
            au = input('What 2d shape would you like to solve today?\n')
            if au == 'T' or 't':
                print('Ok great! You chose to calculate values for a triangle! Enter your base and height values below!')
                b = input('Base: ')
                h = input('Height: ')

                try:
                    b = float(b)
                    h = float(h)
                    print('AREA OF TRIANGLE: ' + str(0.5 * b * h))
                except:
                    print('Enter numerical values for b and h!')

            elif au == 'S' or 's':
                print('Ok great! You chose to calculate values for a square/rectangle! Enter your side length values below!')
                s1 = input('Side length 1: ')
                s2 = input('Side length 2: ')

                try:
                    s1 = float(s1)
                    s2 = float(s2)
                    print('PERIMETER OF RECTANGLE: ' + str(2 * (s1 + s2)))
                    print('AREA OF RECTANGLE: ' + str(s1 * s2))
                except:
                    print('Enter numerical values for s1 and s2!')

            elif au == 'P' or 'p':
                print('Ok great! You chose to calculate values for a parallelogram! Enter your base and height values below!')
                b = input('Base: ')
                h = input('Height: ')

                try:
                    b = float(b)
                    h = float(h)
                    print('AREA OF PARALLELOGRAM: ' + str(b * h))
                except:
                    print('Enter numerical values for b and h!')

            elif au == 'Z' or 'z':
                print('Ok great! You chose to calculate values for a trapezoid! Enter your base1, base2 and height values below!')
                b1 = input('Base 1: ')
                b2 = input('Base 2: ')
                h = input('Height: ')

                try:
                    b1 = float(b1)
                    b2 = float(b2)
                    h = float(h)
                    print('AREA OF TRAPEZOID: ' + str(0.5 * h * (b1 + b2)))
                except:
                    print('Enter numerical values for b1, b2 and h!')

            elif au == 'C' or 'c':
                print('Ok great! You chose to calculate values for a circle! Enter your radius value below!')
                r = input('Radius: ')

                try:
                    r = float(r)
                    print("CIRCUMFERENCE OF CIRCLE: " + str(2 * math.pi * r))
                    print("AREA OF CIRCLE: " + str(r * r * math.pi))
                except:
                    print('Enter numerical values for r!')

            else:
                print('Enter characters EXACTLY as shown above!')

            print("-" * 100)
            print('\n')

        elif bruh == '3d' or bruh == '3D':
            print('T: Pyramid')
            time.sleep(0.25)
            print('C: Cube/Rectangular Prism')
            time.sleep(0.25)
            print('S: Sphere')
            time.sleep(0.25)
            print('N: Cone')
            time.sleep(0.25)
            print('Y: Cylinder')
            time.sleep(0.25)
            print('R: Triangular Prism')
            time.sleep(0.25)
            print('H: Hexagonal Prism')
            time.sleep(0.25)
            print('P: Pentagonal Prism')
            time.sleep(0.25)
            au = input('What 3d shape would you like to solve today?\n')
            if au == 'T' or 't':
                print('Ok great! You chose to calculate values for a pyramid! Enter your length, width and height values below!')
                l = input('Length: ')
                w = input('Width: ')
                h = input('Height: ')

                try:
                    l = float(l)
                    w = float(w)
                    h = float(h)
                    print('SURFACE AREA OF PYRAMID: ' + str((l * w) + l * math.sqrt((w / 2) ** 2 + h ** 2) + w * math.sqrt((l / 2) ** 2 + h ** 2)))
                    print('VOLUME OF PYRAMID: ' + str((l * w * h) / 3))
                except:
                    print('Enter numerical values for l, w and h!')

            elif au == 'C' or 'c':
                print('Ok great! You chose to calculate values for a cube/rectangular prism! Enter your side length values below!')
                s1 = input('Side length 1: ')
                s2 = input('Side length 2: ')
                s3 = input('Side length 3: ')

                try:
                    s1 = float(s1)
                    s2 = float(s2)
                    s3 = float(s3)
                    print('SURFACE AREA OF RECTANGULAR PRISM: ' + str(2 * (s1 * s2 + s1 * s3 + s2 *s3)))
                    print('VOLUME OF RECTANGULAR PRISM: ' + str(s1 * s2 * s3))
                except:
                    print('Enter numerical values for s1, s2 and s3!')

            elif au == 'S' or 's':
                print('Ok great! You chose to calculate values for a SPHERE! Enter your radius value below!')
                r = input('Radius: ')

                try:
                    r = float(r)
                    print('SURFACE AREA OF SPHERE: ' + str(4 * math.pi * r * r))
                    print('VOLUME OF SPHERE: ' + str((4 / 3) * math.pi * r * r * r))
                except:
                    print('Enter numerical values for r!')

            elif au == 'N' or 'n':
                print('Ok great! You chose to calculate values for a CONE! Enter your radius and height values below!')
                r = input('Radius: ')
                h = input('Height: ')

                try:
                    r = float(r)
                    h = float(h)
                    print('SURFACE AREA OF CONE: ' + str((math.pi * r) * (r + math.sqrt(h * h * r * r))))
                    print('VOLUME OF CONE: ' + str((1 / 3) * math.pi * r * r * h)) 
                except:
                    print('Enter numerical values for r and h!')

            elif au == 'Y' or 'y':
                print('Ok great! You chose to calculate values for a CYLINDER! Enter your radius and height values below!')
                r = input('Radius: ')
                h = input('Height: ')

                try:
                    r = float(r)
                    h = float(h)
                    print('SURFACE AREA OF CYLINDER: ' + str((2 * math.pi * r * h) + (2 * math.pi * r * r)))
                    print('VOLUME OF CYLINDER: ' + str(math.pi * r * r * h)) 
                except:
                    print('Enter numerical values for r and h!')

            elif au == 'R' or 'r':
                print('Ok great! You chose to calculate values for a TRIANGULAR PRISM! Enter your triangle\'s side length values and height value below!')
                b1 = input('Side Length 1: ')
                b2 = input('Side Length 2: ')
                b3 = input('Side Length 3: ')
                h = input('Height: ')

                try:
                    b1 = float(b1)
                    b2 = float(b2)
                    b3 = float(b3)
                    h = float(h)
                    s = (b1 + b2 + b3) / 2
                    p = b1 + b2 + b3
                    print('SURFACE AREA OF TRIANGULAR PRISM: ' + str((p * h) + 2 * (math.sqrt(s * (s-b1) * (s-b2) * (s-b3)))))
                    print('VOLUME OF TRIANGULAR PRISM: ' + str((0.25 * h) * math.sqrt(-1 * (b1 ** 4) + 2 * ((b1 * b2) ** 2) + 2 * ((b1 * b3) ** 2) - (b2 ** 4) + 2 * ((b2 * b3) ** 2) - (b3 ** 4)))) 
                except:
                    print('Enter numerical values for b1, b2, b3 and h!')

            elif au == 'H' or 'h':
                print('Ok great! You chose to calculate values for a HEXAGONAL PRISM! Enter your side length and height values below!')
                a = input('Side Length: ')
                h = input('Height: ')

                try:
                    a = float(a)
                    h = float(h)
                    print('SURFACE AREA OF HEXAGONAL PRISM: ' + str((6 * a * h) + (3 * math.sqrt(3) * a * a)))
                    print('VOLUME OF HEXAGONAL PRISM: ' + str(3 * math.sqrt(3) / 2 * a * a * h)) 
                except:
                    print('Enter numerical values for s1 and h!')

            elif au == 'P' or 'p':
                print('Ok great! You chose to calculate values for a PENTAGONAL PRISM! Enter your side length and height values below!')
                a = input('Side Length: ')
                h = input('Height: ')

                try:
                    a = float(a)
                    h = float(h)
                    print('SURFACE AREA OF PENTAGONAL PRISM: ' + str(5 * a * h + (0.5 * math.sqrt(5 * (5 + (2 * math.sqrt(5)))) * a * a)))
                    print('VOLUME OF PENTAGONAL PRISM: ' + str(0.25 * math.sqrt(5 * (5 + (2 * math.sqrt(5)))) * a * a * h)) 
                except:
                    print('Enter numerical values for s1 and h!')

            else:
                print('Enter characters EXACTLY as shown above!')

            print("-" * 100)
            print('\n')
        else:
            print('Please enter a valid character set')
            print("-" * 100)
            print('\n')

# call 'em
splashLauncher()
printLogo()
time.sleep(2)
geoCalc()