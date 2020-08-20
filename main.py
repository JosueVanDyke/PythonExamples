from tkinter import *
from tkinter.ttk import *
from random_functions import *

root = Tk()
root.grid()

root.geometry('1000x700')

Label(root, text = 'The Gang', font = ('Comic Sans', 15)).pack(side = TOP, pady = 10)


photo_Luke = PhotoImage( file = "D:\Pictures\People\\TheBoi.png")
photo_Thomas = PhotoImage(file = "D:\Pictures\People\\thomas.png")
photo_Hobbs = PhotoImage(file = "D:\Pictures\People\\Hobbs.png")
photo_Nowlin = PhotoImage(file = "D:\Pictures\People\\nowlin.png")
photo_Stonks = PhotoImage(file = "D:\Pictures\People\\StonksBoi.png")

btn_Luke = Button(root, image = photo_Luke, command = action_Luke).pack(side = BOTTOM)
btn_Thomas = Button(root, image = photo_Thomas, command = action_Thomas).pack(side = LEFT)
btn_Hobbs = Button(root, image = photo_Hobbs, command = action_Hobbs).pack(side = LEFT)
btn_Nowlin = Button(root, image = photo_Nowlin, command = action_Nowlin).pack(side = LEFT)
btn_Stonks = Button(root, image = photo_Stonks, command = action_Stonks).pack(side = BOTTOM)

root.mainloop()

