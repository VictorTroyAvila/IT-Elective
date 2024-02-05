from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

root = Tk()

item_frame = Frame(root)

root.title('Kiosk')
root.geometry('700x900')
root.resizable(width=False, height=False)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "it_electve"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT Item FROM veryfastfood")

for i in range(4):
  item_frame.grid_columnconfigure(i)

col=0
row=0
for veryfastfood in mycursor:
    for j in range(len(veryfastfood)):
      btn = tk.Button(item_frame, text=veryfastfood[j], wraplength=100, padx=2, pady=2, height=4, width=18, bg='#fab6fa')
      btn.grid(column=col, row=row, sticky='news')
      if col == 4:
        col = 0
        row += 1
      else:
        col += 1
        root.grid_rowconfigure(row, uniform='rows')
        if row == 6 and col == 4:
           row = 2
           col = 3
           break

item_frame.pack(padx=1,pady=1)

root.mainloop()