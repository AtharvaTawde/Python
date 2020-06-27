import Tkinter
import random
# bruh, its me
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 60

def startGame(event):
    if timeleft == 60:
        countdown()
    nextColor()


def nextColor():
    global score
    global timeleft
    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score += 1
        e.delete(0, Tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)


root = Tkinter.Tk()
root.title("COLOR GAME")
root.geometry("420x250")
instructions = Tkinter.Label(root, text="Type in the color of the words, and not the word you see!",
                             font=('Comic Sans MS', 12))
instructions.pack()
scoreLabel = Tkinter.Label(root, text="Press enter to start", font=('Comic Sans MS', 12))
scoreLabel.pack()
timeLabel = Tkinter.Label(root, text="Time left: " + str(timeleft), font=('Comic Sans MS', 12))
timeLabel.pack()
label = Tkinter.Label(root, font=('Comic Sans MS', 60))
label.pack()
e = Tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()
