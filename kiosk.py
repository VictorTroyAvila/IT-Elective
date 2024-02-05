from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import font
import mysql.connector

def cart():
    root.destroy()
    import cart


root = tk.Tk()

item_frame = Frame(root)

root.title('Kiosk')
root.geometry('700x900')
root.config(bg='#fab6fa')
root.resizable(width=False, height=False)

pillow_image = Image.open("D:\Documents\IT-Elective\pics\\one.png")
pillow_image = pillow_image.resize((700,200))
image = ImageTk.PhotoImage(pillow_image)

label = tk.Label(root, image = image)
label.pack()

# Store labels for reference
labels = []

# Labels with click effects
for text, x_position in [('MEALS', 10), ('APPETIZERS', 102), ('DRINKS', 240), ('DESSERTS', 340), ('SNACKS', 464)]:
    label = tk.Label(root, text=text, borderwidth=1, relief='solid', padx=15, pady=2, font=('Poppins', 12, 'bold'), background='WHITE', fg='black', cursor='hand2')
    label.place(x=x_position, y=216)
    labels.append(label)

# Reset all labels to their original colors
def reset_colors():
    for label in labels:
        label.config(background='WHITE', fg='BLACK')

# Change the color of a label on click, resetting if already selected
def change_color(label):
    current_bg = label.cget('background')  # Retrieve current background color
    if current_bg == '#33691E':  # Check if already selected
        general()
        label.config(background='WHITE', fg='BLACK')  # Return to original colors
    else:
        reset_colors()  # Reset all labels
        label.config(background='#33691E', fg='WHITE')  # Highlight the clicked label
        lbl_name = label.cget('text')
        catFil(lbl_name)

# Connect click events to each label
for label in labels:
    label.bind('<Button-1>', lambda e, l=label: change_color(l))


placeorder = tk.Label(root, text='PLACE ORDER - DINE IN', background='#13ab40',font=('Poppins', 10, 'bold'), width=700,padx=12,pady=4, anchor='w')
placeorder.place(x=0,y=780)


quantity = tk.Label(root, text='QUANTITY', background='#fab6fa',font=('Poppins', 10, 'bold'),)
quantity.place(x=100,y=820)


a17 = Image.open("D:\Documents\IT-Elective\pics\\plus.png")
a17 = a17.resize((28,28))
image17 = ImageTk.PhotoImage(a17)

label17 = tk.Label(root, image = image17, borderwidth=0, relief='solid')
label17.place(x=120,y=850)

a18 = Image.open("D:\Documents\IT-Elective\pics\\minus.png")
a18 = a18.resize((28,28))
image18 = ImageTk.PhotoImage(a18)

label18 = tk.Label(root, image = image18, borderwidth=0, relief='solid')
label18.place(x=160,y=850)

quantity1 = tk.Label(root, text='01', background='WHITE',font=('Poppins', 10, 'bold'), borderwidth=1, relief='solid',padx=12, pady=8)
quantity1.place(x=220,y=845)

button1 = tk.Button(root, text='Cancel Order', font=('Poppins', 14), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=26, pady=8)
button1.place(x=320,y=830)
button2 = tk.Button(root, text='Place Order', font=('Poppins', 14), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=26, pady=8, command=cart)
button2.place(x=520,y=830)

button = tk.Button(root, text='BACK', font=('Poppins', 12, 'bold'), background='#33691E', fg='white', cursor='hand2',borderwidth=0, padx=32, pady=2)
button.pack(side=tk.TOP,anchor=tk.NE, padx=10, pady=10)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "it_electve"
)

def general():
    Meals = mydb.cursor()
    Meals.execute("SELECT Item FROM veryfastfood")

    col=0
    row=0
    for veryfastfood in Meals:
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

def catFil(lbl_name):
    for widgets in item_frame.winfo_children():
      widgets.destroy()

    if (lbl_name == "MEALS"):
        for widgets in item_frame.winfo_children():
            widgets.destroy()
        
        Meals = mydb.cursor()
        Meals.execute("SELECT Item FROM veryfastfood WHERE Category = 'Meals'")

        col=0
        row=0
        for veryfastfood in Meals:
            for j in range(len(veryfastfood)):
            
                btn = tk.Button(item_frame, text=veryfastfood[j], wraplength=100, padx=2, pady=2, height=4, width=18, bg='#fab6fa')
                btn.grid(column=col, row=row, sticky='news')
            if col == 4:
                col = 0
                row += 1
            else:
                col += 1
                root.grid_rowconfigure(row, uniform='rows')

        item_frame.pack(padx=1,pady=1)

    elif (lbl_name == 'APPETIZERS'):
        for widgets in item_frame.winfo_children():
            widgets.destroy()
        
        Appetizers = mydb.cursor()
        Appetizers.execute("SELECT Item FROM veryfastfood WHERE Category = 'Appetizers'")

        col=0
        row=0
        for veryfastfood in Appetizers:
            for j in range(len(veryfastfood)):
            
                btn = tk.Button(item_frame, text=veryfastfood[j], wraplength=100, padx=2, pady=2, height=4, width=18, bg='#fab6fa')
                btn.grid(column=col, row=row, sticky='news')
            if col == 4:
                col = 0
                row += 1
            else:
                col += 1
                root.grid_rowconfigure(row, uniform='rows')

        item_frame.pack(padx=1,pady=1)

    elif (lbl_name == 'DRINKS'):
        for widgets in item_frame.winfo_children():
            widgets.destroy()
        
        Drinks = mydb.cursor()
        Drinks.execute("SELECT Item FROM veryfastfood WHERE Category = 'Drinks'")

        col=0
        row=0
        for veryfastfood in Drinks:
            for j in range(len(veryfastfood)):
            
                btn = tk.Button(item_frame, text=veryfastfood[j], wraplength=100, padx=2, pady=2, height=4, width=18, bg='#fab6fa')
                btn.grid(column=col, row=row, sticky='news')
            if col == 4:
                col = 0
                row += 1
            else:
                col += 1
                root.grid_rowconfigure(row, uniform='rows')

        item_frame.pack(padx=1,pady=1)

    elif (lbl_name == 'DESSERTS'):
        for widgets in item_frame.winfo_children():
            widgets.destroy()
        
        Dessert = mydb.cursor()
        Dessert.execute("SELECT Item FROM veryfastfood WHERE Category = 'Dessert'")

        col=0
        row=0
        for veryfastfood in Dessert:
            for j in range(len(veryfastfood)):
            
                btn = tk.Button(item_frame, text=veryfastfood[j], wraplength=100, padx=2, pady=2, height=4, width=18, bg='#fab6fa')
                btn.grid(column=col, row=row, sticky='news')
            if col == 4:
                col = 0
                row += 1
            else:
                col += 1
                root.grid_rowconfigure(row, uniform='rows')

        item_frame.pack(padx=1,pady=1)

    elif (lbl_name == 'SNACKS'):
        for widgets in item_frame.winfo_children():
            widgets.destroy()
        
        Snack = mydb.cursor()
        Snack.execute("SELECT Item FROM veryfastfood WHERE Category = 'Snack'")

        col=0
        row=0
        for veryfastfood in Snack:
            for j in range(len(veryfastfood)):
            
                btn = tk.Button(item_frame, text=veryfastfood[j], wraplength=100, padx=2, pady=2, height=4, width=18, bg='#fab6fa')
                btn.grid(column=col, row=row, sticky='news')
            if col == 4:
                col = 0
                row += 1
            else:
                col += 1
                root.grid_rowconfigure(row, uniform='rows')
        
        item_frame.pack(padx=1,pady=1)

root.mainloop()