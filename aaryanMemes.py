from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Welcome to Aaryan's hidden Meme Page!\n")
text.insert(INSERT, "Aaryan's fresh baked memes, right to you front door. \n(This isn't even a complete sentence BTW).\n")
text.insert(INSERT, '                                      *                     \n')
text.insert(INSERT, '   (                                (  `\n')
text.insert(INSERT, '   )\        ) (   (       )         )\))(    (    )     (\n')
text.insert(INSERT, ' ((((_)(   ( /( )(  )\ ) ( /(  (     ((_)()\  ))\  (     ))\(\n')
text.insert(INSERT, "  )\ _ ) \ )(_)|()\(()/( )(_)) )\ )  (_()((_)/((_) )\  '/((_)\n")
text.insert(INSERT, ' (_)_\(_ |(_)_ ((_))(_)|(_)_ _(_/(  |  \/  (_)) _((_))(_))((_)\n')
text.insert(INSERT, "  / _ \  / _` | '_| || / _` | ' \)) | |\/| / -_) '  \() -_|_-<\n")
text.insert(INSERT, " /_/ \_\ \__,_|_|  \_, \__,_|_||_|  |_|  |_\___|_|_|_|\___/__/\n")
text.insert(INSERT, "                   |__/\n")
text.pack()

text.tag_add("here", "1.0", "1.1000")
text.tag_add('red', '4.0', '12.1000')
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config('red', background='white', foreground='red')
text.config(state=DISABLED)
root.mainloop()










