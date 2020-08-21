import tkinter as tk
from tkinter import messagebox
from tkinter.tix import Balloon
from tkinter.ttk import *
import RandomClasses

quotes = RandomClasses

tk.Label(text = 'The Gang', font = ('Comic Sans', 15)).grid(row=0, column=1)

photo_Luke = tk.PhotoImage( file = "D:\\Pictures\\People\\TheBoi.png")
photo_Thomas = tk.PhotoImage(file = "D:\\Pictures\\People\\thomas.png")
photo_Hobbs = tk.PhotoImage(file = "D:\\Pictures\\People\\Hobbs.png")
photo_Nowlin = tk.PhotoImage(file = "D:\\Pictures\\People\\nowlin.png")
photo_Stonks = tk.PhotoImage(file = "D:\\Pictures\\People\\StonksBoi.png")
photo_Kang = tk.PhotoImage(file = "D:\\Pictures\\People\\kang.png")

btn_Luke = tk.Button(image = photo_Luke, command = quotes.action_Luke).grid(row=1, column=0, padx = 10, pady = 10)
btn_Thomas = tk.Button(image = photo_Thomas, command = quotes.action_Thomas).grid(row=1, column=1, padx = 10, pady = 10)
btn_Hobbs = tk.Button(image = photo_Hobbs, command = quotes.action_Hobbs).grid(row=1, column=2, padx = 10, pady = 10)
btn_Nowlin = tk.Button(image = photo_Nowlin, command = quotes.action_Nowlin).grid(row=2, column=0, padx = 10, pady = 10)
btn_Stonks = tk.Button(image = photo_Stonks, command = quotes.action_Stonks).grid(row=2, column=1, padx = 10, pady = 10)
btn_Kang = tk.Button(image = photo_Kang, command = quotes.action_Kang).grid(row=2, column=2, padx = 10, pady = 10)

messagebox.showinfo("Welcome!","Welcome to my program!")

#balloon = Balloon(bg="white", title = "help")
#balloon.bind_widget(btn_Luke, baloonmsg = "HELP!! I'm being misquoted!")

tk.mainloop()

