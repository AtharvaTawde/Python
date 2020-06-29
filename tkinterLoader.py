from tkinter import *

def onclick():
   pass

root = Tk()
text = Text(root)
text.insert(INSERT, "Welcome to GeoCalc!")
text.insert(INSERT, '\n')
text.insert(INSERT, " _____            _____       _\n")
text.insert(INSERT, "|  __ \          /  __ \     | |\n")
text.insert(INSERT, '| |  \/ ___  ___ | /  \/ __ _| | ___\n')
text.insert(INSERT, '| | __ / _ \/ _ \| |    / _` | |/ __|\n')
text.insert(INSERT, '| |_\ \  __/ (_) | \__/\ (_| | | (\n')
text.insert(INSERT, ' \____/\___|\___/ \____/\__,_|_|\___|\n')
text.insert(INSERT, 'Created by Atharva Tawde :0\n')
text.insert(INSERT, '\n')
text.insert(INSERT,
            'Before using however, note that this software cannot be redistributed for personal profit, but may be distributed for academic use.\n')
text.insert(INSERT, 'To complete the loading of the application, X out of this tab now!')
text.pack()

text.tag_add("here", "1.0", "1.19")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")
text.config(state=DISABLED)
root.mainloop()