import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import font

def payment():
    root.destroy()
    import payment

def back():
    root.destroy()
    import kiosk

root = tk.Tk()

root.title('Kiosk')
root.geometry('700x900')
root.config(bg='#fab6fa')
root.resizable(width=False, height=False)

pillow_image = Image.open("D:\Documents\IT-Elective\pics\one.png")
pillow_image = pillow_image.resize((500,200))
image = ImageTk.PhotoImage(pillow_image)

label = tk.Label(root, image = image, borderwidth=0)
label.pack(padx=10, pady=24)

italic_font = font.Font(family="Inter", size=20, slant="italic")

titletext = tk.Label(root,text='REVIEW MY ORDER', font=('Inter', 20, 'bold','italic'), bg='#fab6fa')
titletext.pack(padx=10,pady=10)


frame1 = tk.Frame(root, width=450, height=170, bg='WHITE',borderwidth=2, relief='solid')
frame1.pack(padx=20,pady=20)


l1 = Image.open("D:\Documents\IT-Elective\pics\dashed.png")
l1 = l1.resize((446,20))
image1 = ImageTk.PhotoImage(l1)

label1 = tk.Label(root, image = image1, borderwidth=0, bg="WHITE")
label1.place(x=127,y=360)

text1 = tk.Label(root,text='1x Burger With Fries', font=('Inter', 14, 'bold'), bg='WHITE')
text1.place(x=135,y=335)
text2 = tk.Label(root,text='PHP 129.00', font=('Inter', 14, 'bold'), bg='WHITE')
text2.place(x=450,y=335)
text3 = tk.Label(root,text='Medium Coke 16oz', font=('Inter', 14, 'bold'), bg='WHITE')
text3.place(x=135,y=380)
text4 = tk.Label(root,text='* No ice', font=('Inter', 14, 'bold'), bg='WHITE')
text4.place(x=150,y=405)

l2 = Image.open("D:\Documents\IT-Elective\pics\dashed.png")
l2 = l2.resize((446,20))
image2 = ImageTk.PhotoImage(l2)

label2 = tk.Label(root, image = image2, borderwidth=0, bg="WHITE")
label2.place(x=127,y=430)

button1 = tk.Button(root, text='Remove', font=('inter', 11, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=20, pady=4)
button1.place(x=150,y=453)
button2 = tk.Button(root, text='Edit', font=('inter', 11, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=32, pady=4)
button2.place(x=450,y=453)


a18 = Image.open("D:\Documents\IT-Elective\pics\minus.png")
a18 = a18.resize((28,28))
image18 = ImageTk.PhotoImage(a18)

label18 = tk.Label(root, image = image18, borderwidth=0, relief='solid')
label18.place(x=300,y=455)

quantity1 = tk.Label(root, text='01', background='WHITE',font=('Inter', 10, 'bold'), borderwidth=1, relief='solid',padx=12, pady=4)
quantity1.place(x=335,y=456)

a17 = Image.open("D:\Documents\IT-Elective\pics\plus.png")
a17 = a17.resize((28,28))
image17 = ImageTk.PhotoImage(a17)

label17 = tk.Label(root, image = image17, borderwidth=0, relief='solid')
label17.place(x=380,y=455)


frame2 = tk.Frame(root, width=450, height=170, bg='WHITE',borderwidth=2, relief='solid')
frame2.pack(padx=20,pady=20)


text5 = tk.Label(root,text='1x 2 piece Chicken', font=('Inter', 14, 'bold'), bg='WHITE')
text5.place(x=135,y=545)
text6 = tk.Label(root,text='PHP 109.00', font=('Inter', 14, 'bold'), bg='WHITE')
text6.place(x=450,y=545)


l3 = Image.open("D:\Documents\IT-Elective\pics\dashed.png")
l3 = l2.resize((446,20))
image3 = ImageTk.PhotoImage(l3)

label3 = tk.Label(root, image = image3, borderwidth=0, bg="WHITE")
label3.place(x=127,y=570)

l4 = Image.open("D:\Documents\IT-Elective\pics\dashed.png")
l4 = l4.resize((446,20))
image4 = ImageTk.PhotoImage(l4)

label4 = tk.Label(root, image = image4, borderwidth=0, bg="WHITE")
label4.place(x=127,y=640)

button1 = tk.Button(root, text='Remove', font=('inter', 11, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=20, pady=4)
button1.place(x=150,y=663)
button2 = tk.Button(root, text='Edit', font=('inter', 11, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=32, pady=4)
button2.place(x=450,y=663)


a19 = Image.open("D:\Documents\IT-Elective\pics\minus.png")
a19 = a19.resize((28,28))
image19 = ImageTk.PhotoImage(a19)

label19 = tk.Label(root, image = image19, borderwidth=0, relief='solid')
label19.place(x=300,y=665)

quantity1 = tk.Label(root, text='01', background='WHITE',font=('Inter', 10, 'bold'), borderwidth=1, relief='solid',padx=12, pady=4)
quantity1.place(x=335,y=666)

a20 = Image.open("D:\Documents\IT-Elective\pics\plus.png")
a20 = a20.resize((28,28))
image20 = ImageTk.PhotoImage(a20)

label20 = tk.Label(root, image = image20, borderwidth=0, relief='solid')
label20.place(x=380,y=665)


l4 = tk.Label(root, width=700, height=1, bg='#13ab40')
l4.place(x=0,y=770)

button3 = tk.Button(root, text='Back', font=('inter', 14, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=100, pady=8, command= back)
button3.place(x=70,y=820)
button4 = tk.Button(root, text='Proceed To Checkout', font=('inter', 14, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=32, pady=8, command= payment)
button4.place(x=370,y=820)

root.mainloop()