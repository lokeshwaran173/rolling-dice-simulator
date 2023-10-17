#PythonGeeks-Dice Rolling using Gui

#import libraries
import tkinter
from PIL import Image,ImageTk
import random

#top level widgets which represents the main window of the application
from PIL.ImageTk import PhotoImage

root=tkinter.Tk()
root.geometry('400x400')
root.title("PythonGeeks-Roll the Dice")

#images
dice=[r'C:/Users/DELL/OneDrive/Pictures/Screenshots/die1.png',r'C:/Users/DELL/OneDrive/Pictures/Screenshots/die2.png',r'C:/Users/DELL/OneDrive/Pictures/Screenshots/die3.png',r'C:/Users/DELL/OneDrive/Pictures/Screenshots/die4.png',r'C:/Users/DELL/OneDrive/Pictures/Screenshots/die5.png',r'C:/Users/DELL/OneDrive/Pictures/Screenshots/die6.png',]

#simulating the dice with random variables 1 to 6 and generate image
image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
#constructing a Label widget for image
label1=tkinter.Label(root,image=image1)
label1.image=image1
#packing a widget in the parent widget
label1.pack(expand=True)

#function activated by button
def rolling_dice():
    image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #update image
    label1.configure(image=image1)
    #keep a reference
    label1.image=image1

#adding buttons,and command will use rolling_dice function
button=tkinter.Button(root,text="Roll the dice",fg="green",command=rolling_dice)
#pack a widget in parent widget
button.pack(expand="True")
#call the mainloop

root.mainloop()