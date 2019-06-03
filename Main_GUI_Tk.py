from tkinter import *

from Speech_Recognition.JARVIS_file import JARVIS

# Global constants
WIN_WIDTH = 720/2
WIN_HEIGHT = 1280/2
WIN_POS_X = 900
WIN_POS_Y = 200

# Load an instance of JARVIS class in JARVIS_file
Jojo = JARVIS()

# Main window
root = Tk()
root.geometry('{}x{}+{}+{}'.format(int(WIN_WIDTH), int(WIN_HEIGHT), WIN_POS_X, WIN_POS_Y))
root.title("JARVIS")
root.bind('q', quit)

# Load JARVIS.png
jar_img = PhotoImage(file='jarvis-png-3.png')

# Icon
root.tk.call('wm', 'iconphoto', root._w, jar_img)

# Creating buttons
button_5 = Button(root, image=jar_img, command=Jojo.JARVIS_main)    # bitmap for image background
button_6 = Button(root, text='QUIT', fg='white', bg='red', width=30, pady=5, command=quit)

# Showing buttons
button_5.place(relx=0.5, rely=0.5, anchor=CENTER)
button_6.place(relx=0.5, rely=0.98, anchor=S)

# Main loop. Run the program until a close action is triggered
root.mainloop()
print("DONE!")