from tkinter import *
from PIL import Image, ImageTk

from Speech_Recognition.main_gui_helper import JARVIS, AIDA

# Global constants
WIN_WIDTH = 720/2
WIN_HEIGHT = 1280/2
WIN_POS_X = 900
WIN_POS_Y = 200

# Load an instance of JARVIS and AIDA class in main_gui_helper
Jojo = JARVIS()
aida = AIDA()

# Main window
root = Tk()
root.geometry('{}x{}+{}+{}'.format(int(WIN_WIDTH), int(WIN_HEIGHT), WIN_POS_X, WIN_POS_Y))
root.title("AIDA")
root.bind('q', quit)

# Load icons
shield_img = PhotoImage(file='shield.png')
aida_img = ImageTk.PhotoImage(Image.open('shield.png').resize((200, 200)))
jar_img = ImageTk.PhotoImage(Image.open('jarvis.png').resize((200, 200)))

# Window icon
root.tk.call('wm', 'iconphoto', root._w, shield_img)

# Creating buttons
button_5 = Button(root, image=jar_img, command=Jojo.JARVIS_main) # AIDA button
button_7 = Button(root, image=aida_img, command=aida.AIDA_main) # AIDA button

button_6 = Button(root, text='QUIT', fg='white', bg='red', width=30, pady=5, command=quit)

# Showing buttons
button_5.place(relx=0.5, rely=0.3, anchor=CENTER)
button_7.place(relx=0.5, rely=0.7, anchor=CENTER)

button_6.place(relx=0.5, rely=0.98, anchor=S)

# Main loop. Run the program until a close action is triggered
root.mainloop()
print("DONE!")