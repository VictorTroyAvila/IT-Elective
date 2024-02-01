from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import font
import cart


def cart():
    root.destroy()
    exec(cart)


root = tk.Tk()

root.title('Kiosk')
root.geometry('700x900')
root.config(bg='#fab6fa')
root.resizable(width=False, height=False)

pillow_image = Image.open("D:\Documents\IT-Elective\pics\\one.png")
pillow_image = pillow_image.resize((700,200))
image = ImageTk.PhotoImage(pillow_image)

label = tk.Label(root, image = image)
label.pack()


a1 = Image.open("D:\Documents\IT-Elective\pics\\A1.png")
a1 = a1.resize((140,80))
image1 = ImageTk.PhotoImage(a1)

label1 = tk.Label(root, image = image1, borderwidth=0, relief='flat', bg='#fab6fa')
label1.place(x=10,y=260)

a2 = Image.open("D:\Documents\IT-Elective\pics\\A2.png")
a2 = a2.resize((140,80))
image2 = ImageTk.PhotoImage(a2)

label2 = tk.Label(root, image = image2, borderwidth=1, relief='flat', bg='#fab6fa')
label2.place(x=180,y=260)

a3 = Image.open("D:\Documents\IT-Elective\pics\\A3.png")
a3 = a3.resize((140,80))
image3 = ImageTk.PhotoImage(a3)

label3 = tk.Label(root, image = image3, borderwidth=1, relief='flat', bg='#fab6fa')
label3.place(x=353,y=260)

a31 = Image.open("D:\Documents\IT-Elective\pics\\A4.png")
a31 = a31.resize((140,80))
image31 = ImageTk.PhotoImage(a31)

label31 = tk.Label(root, image = image31, borderwidth=1, relief='flat', bg='#fab6fa')
label31.place(x=540,y=260)




a4 = Image.open("D:\Documents\IT-Elective\pics\\B1.png")
a4 = a4.resize((140,80))
image4 = ImageTk.PhotoImage(a4)

label4 = tk.Label(root, image = image4, borderwidth=1, relief='flat', bg='#fab6fa')
label4.place(x=10,y=369)

a5 = Image.open("D:\Documents\IT-Elective\pics\\B2.png")
a5 = a5.resize((140,80))
image5 = ImageTk.PhotoImage(a5)

label5 = tk.Label(root, image = image5, borderwidth=1, relief='flat', bg='#fab6fa')
label5.place(x=180,y=369)

a6 = Image.open("D:\Documents\IT-Elective\pics\\B3.png")
a6 = a6.resize((140,80))
image6 = ImageTk.PhotoImage(a6)

label6 = tk.Label(root, image = image6, borderwidth=1, relief='flat', bg='#fab6fa')
label6.place(x=353,y=369)

a61 = Image.open("D:\Documents\IT-Elective\pics\\B4.png")
a61 = a61.resize((140,80))
image61 = ImageTk.PhotoImage(a61)

label61 = tk.Label(root, image = image61, borderwidth=1, relief='flat', bg='#fab6fa')
label61.place(x=540,y=369)




a7 = Image.open("D:\Documents\IT-Elective\pics\\C1.png")
a7 = a7.resize((140,80))
image7 = ImageTk.PhotoImage(a7)

label7 = tk.Label(root, image = image7, borderwidth=1, relief='flat', bg='#fab6fa')
label7.place(x=10,y=466.5)

a8 = Image.open("D:\Documents\IT-Elective\pics\\C2.png")
a8 = a8.resize((140,80))
image8 = ImageTk.PhotoImage(a8)

label8 = tk.Label(root, image = image8, borderwidth=1, relief='flat', bg='#fab6fa')
label8.place(x=180,y=466.5)

a9 = Image.open("D:\Documents\IT-Elective\pics\\C3.png")
a9 = a9.resize((140,80))
image9 = ImageTk.PhotoImage(a9)

label9 = tk.Label(root, image = image9, borderwidth=1, relief='flat', bg='#fab6fa')
label9.place(x=353,y=466.5)

a91 = Image.open("D:\Documents\IT-Elective\pics\\C4.png")
a91 = a91.resize((140,80))
image91 = ImageTk.PhotoImage(a91)

label91 = tk.Label(root, image = image91, borderwidth=1, relief='flat', bg='#fab6fa')
label91.place(x=540,y=466.5)



a10 = Image.open("D:\Documents\IT-Elective\pics\\D1.png")
a10 = a10.resize((140,90))
image10 = ImageTk.PhotoImage(a10)

label10 = tk.Label(root, image = image10, borderwidth=1, relief='flat', bg='#fab6fa')
label10.place(x=10,y=563.5)

a11 = Image.open("D:\Documents\IT-Elective\pics\\D2.png")
a11 = a11.resize((140,90))
image11 = ImageTk.PhotoImage(a11)

label11 = tk.Label(root, image = image11, borderwidth=1, relief='flat', bg='#fab6fa')
label11.place(x=180,y=563.5)

a12 = Image.open("D:\Documents\IT-Elective\pics\\D3.png")
a12 = a12.resize((140,90))
image12 = ImageTk.PhotoImage(a12)

label12 = tk.Label(root, image = image12, borderwidth=1, relief='flat', bg='#fab6fa')
label12.place(x=353,y=563.5)

a121 = Image.open("D:\Documents\IT-Elective\pics\\D4.png")
a121 = a121.resize((140,90))
image121 = ImageTk.PhotoImage(a121)

label121 = tk.Label(root, image = image121, borderwidth=1, relief='flat', bg='#fab6fa')
label121.place(x=540,y=563.5)




a13 = Image.open("D:\Documents\IT-Elective\pics\\E1.png")
a13 = a13.resize((140,90))
image13 = ImageTk.PhotoImage(a13)

label13 = tk.Label(root, image = image13, borderwidth=1, relief='flat', bg='#fab6fa')
label13.place(x=10,y=670.5)

a14 = Image.open("D:\Documents\IT-Elective\pics\\E2.png")
a14 = a14.resize((140,90))
image14 = ImageTk.PhotoImage(a14)

label14 = tk.Label(root, image = image14, borderwidth=1, relief='flat', bg='#fab6fa')
label14.place(x=180,y=670.5)


a15 = Image.open("D:\Documents\IT-Elective\pics\\E3.png")
a15 = a15.resize((140,90))
image15 = ImageTk.PhotoImage(a15)

label15 = tk.Label(root, image = image15, borderwidth=1, relief='flat', bg='#fab6fa')
label15.place(x=353,y=670.5)

a151 = Image.open("D:\Documents\IT-Elective\pics\\E4.png")
a151 = a151.resize((140,90))
image151 = ImageTk.PhotoImage(a151)

label151 = tk.Label(root, image = image151, borderwidth=1, relief='flat', bg='#fab6fa')
label151.place(x=540,y=670.5)



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
        label.config(background='WHITE', fg='BLACK')  # Return to original colors
    else:
        reset_colors()  # Reset all labels
        label.config(background='#33691E', fg='WHITE')  # Highlight the clicked label

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


meal1 = tk.Label(root, text='A1-Burger with Fries', background='#fab6fa',font=('Poppins', 7, 'bold'),)
meal1.place(x=28,y=342)
meal2 = tk.Label(root, text='A2-Spaghetti with Chicken', background='#fab6fa',font=('Poppins', 7, 'bold'),)
meal2.place(x=189,y=342)
meal3 = tk.Label(root, text='A32-piece Chicken with \n Mashed Potato', background='#fab6fa',font=('Poppins', 7, 'bold'),)
meal3.place(x=370,y=342)
meal4 = tk.Label(root, text='A4-Bangsilog', background='#fab6fa',font=('Poppins', 7, 'bold'),)
meal4.place(x=580,y=342)


appe1 = tk.Label(root, text='B1-Salad', background='#fab6fa',font=('Poppins', 7, 'bold'),)
appe1.place(x=60,y=451)
appe2 = tk.Label(root, text='B2-Chicken with Fries', background='#fab6fa',font=('Poppins', 7, 'bold'),)
appe2.place(x=199,y=451)
appe3 = tk.Label(root, text='B3-Bucket of Fries', background='#fab6fa',font=('Poppins', 7, 'bold'),)
appe3.place(x=380,y=451)
appe4 = tk.Label(root, text='B4-Ham & Egg Burger', background='#fab6fa',font=('Poppins', 7, 'bold'),)
appe4.place(x=560,y=451)

drink1 = tk.Label(root, text='C1-Coke, Fanta, Sprite, Pepsi', background='#fab6fa',font=('Poppins', 7, 'bold'),)
drink1.place(x=11,y=547.5)
drink2 = tk.Label(root, text='C2-Coke Float', background='#fab6fa',font=('Poppins', 7, 'bold'),)
drink2.place(x=220,y=547.5)
drink3 = tk.Label(root, text='C3-Iced Coffee', background='#fab6fa',font=('Poppins', 7, 'bold'),)
drink3.place(x=390,y=547.5)
drink4 = tk.Label(root, text='C4-Lemonade', background='#fab6fa',font=('Poppins', 7, 'bold'),)
drink4.place(x=580,y=547.5)

dessert1 = tk.Label(root, text='D1-Apple Pie', background='#fab6fa',font=('Poppins', 7, 'bold'),)
dessert1.place(x=50,y=654.5)
dessert2 = tk.Label(root, text='D2-Cupcakes', background='#fab6fa',font=('Poppins', 7, 'bold'),)
dessert2.place(x=220,y=654.5)
dessert3 = tk.Label(root, text='D3-Ice Cream', background='#fab6fa',font=('Poppins', 7, 'bold'),)
dessert3.place(x=390,y=654.5)
dessert4 = tk.Label(root, text='D4-Matcha Flurry', background='#fab6fa',font=('Poppins', 7, 'bold'),)
dessert4.place(x=573,y=654.5)

snack1 = tk.Label(root, text='E1-Hotdot Sandwich', background='#fab6fa',font=('Poppins', 7, 'bold'),)
snack1.place(x=30,y=762)
snack2 = tk.Label(root, text='E2-Fries and Nuggets', background='#fab6fa',font=('Poppins', 7, 'bold'),)
snack2.place(x=200,y=762)
snack3 = tk.Label(root, text='E3-6 Pieces Nuggets with Fries', background='#fab6fa',font=('Poppins', 7, 'bold'),)
snack3.place(x=352,y=762)
snack4 = tk.Label(root, text='E4-Sisig', background='#fab6fa',font=('Poppins', 7, 'bold'),)
snack4.place(x=590,y=762)

price1 = tk.Label(root, text='₱129', background='WHITE',font=('Poppins', 7, 'bold'),)
price1.place(x=117,y=265)
price2 = tk.Label(root, text='₱159', background='WHITE',font=('Poppins', 7, 'bold'),)
price2.place(x=285,y=265)
price3 = tk.Label(root, text='₱201', background='WHITE',font=('Poppins', 7, 'bold'),)
price3.place(x=458,y=265)
price31 = tk.Label(root, text='₱120', background='WHITE',font=('Poppins', 7, 'bold'),)
price31.place(x=647,y=265)


price4 = tk.Label(root, text='₱150', background='WHITE',font=('Poppins', 7, 'bold'),)
price4.place(x=117,y=374)
price5 = tk.Label(root, text='₱130', background='WHITE',font=('Poppins', 7, 'bold'),)
price5.place(x=285,y=374)
price6 = tk.Label(root, text='₱105', background='WHITE',font=('Poppins', 7, 'bold'),)
price6.place(x=458,y=374)
price61 = tk.Label(root, text='₱100', background='WHITE',font=('Poppins', 7, 'bold'),)
price61.place(x=647,y=374)

price7 = tk.Label(root, text='₱90', background='WHITE',font=('Poppins', 7, 'bold'),)
price7.place(x=120,y=471)
price8 = tk.Label(root, text='₱109', background='WHITE',font=('Poppins', 7, 'bold'),)
price8.place(x=285,y=471)
price8 = tk.Label(root, text='₱115', background='WHITE',font=('Poppins', 7, 'bold'),)
price8.place(x=458,y=471)
price81 = tk.Label(root, text='₱80', background='WHITE',font=('Poppins', 7, 'bold'),)
price81.place(x=649,y=471)

price9 = tk.Label(root, text='₱130', background='WHITE',font=('Poppins', 7, 'bold'),)
price9.place(x=115,y=569)
price10 = tk.Label(root, text='₱100', background='WHITE',font=('Poppins', 7, 'bold'),)
price10.place(x=285,y=569)
price11 = tk.Label(root, text='₱60', background='WHITE',font=('Poppins', 7, 'bold'),)
price11.place(x=464,y=569)
price111 = tk.Label(root, text='₱105', background='WHITE',font=('Poppins', 7, 'bold'),)
price111.place(x=645,y=569)

price12 = tk.Label(root, text='₱112', background='WHITE',font=('Poppins', 7, 'bold'),)
price12.place(x=115,y=675)
price13 = tk.Label(root, text='₱145', background='WHITE',font=('Poppins', 7, 'bold'),)
price13.place(x=285,y=675)
price14 = tk.Label(root, text='₱120', background='WHITE',font=('Poppins', 7, 'bold'),)
price14.place(x=458,y=675)
price15 = tk.Label(root, text='₱299', background='WHITE',font=('Poppins', 7, 'bold'),)
price15.place(x=645,y=675)



root.mainloop()