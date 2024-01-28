from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import font

class Extra(tk.Toplevel):
    def __init__(cart):
        super().__init__()
        root.destroy()

        import tkinter as tk
        from PIL import Image, ImageTk

        cart = tk.Tk()
        
        cart.title('Cart')
        cart.geometry('700x900')
        cart.config(bg='#fab6fa')
        cart.resizable(width=False, height=False)

        pillow_image = Image.open("D:\Documents\IT-Elective\pics\one.png")
        pillow_image = pillow_image.resize((500,200))
        image = ImageTk.PhotoImage(pillow_image)

        label = tk.Label(cart, image = image, borderwidth=0)
        label.pack(padx=10, pady=24)

        # Label(cart,text='* No ice', font=('Inter', 14, 'bold'), bg='WHITE')
        # text4.place(x=150,y=405)

        # l2 = Image# italic_font = font.Font(family="Inter", size=20, slant="italic")

        titletext = tk.Label(cart,text='REVIEW MY ORDER', font=('Inter', 20, 'bold','italic'), bg='#fab6fa')
        titletext.pack(padx=10,pady=10)


        frame1 = tk.Frame(cart, width=450, height=170, bg='WHITE',borderwidth=2, relief='solid')
        frame1.pack(padx=20,pady=20)


        l1 = Image.open("D:\Documents\IT-Elective\pics\dashed.png")
        l1 = l1.resize((446,20))
        image1 = ImageTk.PhotoImage(l1)

        label1 = tk.Label(cart, image = image1, borderwidth=0, bg="WHITE")
        label1.place(x=127,y=360)

        text1 = tk.Label(cart,text='1x Burger With Fries', font=('Inter', 14, 'bold'), bg='WHITE')
        text1.place(x=135,y=335)
        text2 = tk.Label(cart,text='PHP 129.00', font=('Inter', 14, 'bold'), bg='WHITE')
        text2.place(x=450,y=335)
        text3 = tk.Label(cart,text='Medium Coke 16oz', font=('Inter', 14, 'bold'), bg='WHITE')
        text3.place(x=135,y=380)
        text4 = tk.open("D:\Documents\IT-Elective\pics\dashed.png")
        l2 = l2.resize((446,20))
        image2 = ImageTk.PhotoImage(l2)

        label2 = tk.Label(cart, image = image2, borderwidth=0, bg="WHITE")
        label2.place(x=127,y=430)

        button1 = tk.Button(cart, text='Remove', font=('inter', 11, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=20, pady=4)
        button1.place(x=150,y=453)
        button2 = tk.Button(cart, text='Edit', font=('inter', 11, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=32, pady=4)
        button2.place(x=450,y=453)


        a18 = Image.open("D:\Documents\IT-Elective\pics\minus.png")
        a18 = a18.resize((28,28))
        image18 = ImageTk.PhotoImage(a18)

        label18 = tk.Label(cart, image = image18, borderwidth=0, relief='solid')
        label18.place(x=300,y=455)

        quantity1 = tk.Label(cart, text='01', background='WHITE',font=('Inter', 10, 'bold'), borderwidth=1, relief='solid',padx=12, pady=4)
        quantity1.place(x=335,y=456)

        a17 = Image.open("D:\Documents\IT-Elective\pics\plus.png")
        a17 = a17.resize((28,28))
        image17 = ImageTk.PhotoImage(a17)

        label17 = tk.Label(cart, image = image17, borderwidth=0, relief='solid')
        label17.place(x=380,y=455)


        frame2 = tk.Frame(cart, width=450, height=170, bg='WHITE',borderwidth=2, relief='solid')
        frame2.pack(padx=20,pady=20)


        text5 = tk.Label(cart,text='1x 2 piece Chicken', font=('Inter', 14, 'bold'), bg='WHITE')
        text5.place(x=135,y=545)
        text6 = tk.Label(cart,text='PHP 109.00', font=('Inter', 14, 'bold'), bg='WHITE')
        text6.place(x=450,y=545)


        l3 = Image.open("D:\Documents\IT-Elective\pics\dashed.png")
        l3 = l2.resize((446,20))
        image3 = ImageTk.PhotoImage(l3)

        label3 = tk.Label(cart, image = image3, borderwidth=0, bg="WHITE")
        label3.place(x=127,y=570)

        l4 = Image.open("D:\Documents\IT-Elective\pics\dashed.png")
        l4 = l4.resize((446,20))
        image4 = ImageTk.PhotoImage(l4)

        label4 = tk.Label(cart, image = image4, borderwidth=0, bg="WHITE")
        label4.place(x=127,y=640)

        button1 = tk.Button(cart, text='Remove', font=('inter', 11, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=20, pady=4)
        button1.place(x=150,y=663)
        button2 = tk.Button(cart, text='Edit', font=('inter', 11, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=32, pady=4)
        button2.place(x=450,y=663)


        a19 = Image.open("D:\Documents\IT-Elective\pics\minus.png")
        a19 = a19.resize((28,28))
        image19 = ImageTk.PhotoImage(a19)

        label19 = tk.Label(cart, image = image19, borderwidth=0, relief='solid')
        label19.place(x=300,y=665)

        quantity1 = tk.Label(cart, text='01', background='WHITE',font=('Inter', 10, 'bold'), borderwidth=1, relief='solid',padx=12, pady=4)
        quantity1.place(x=335,y=666)

        a20 = Image.open("D:\Documents\IT-Elective\pics\plus.png")
        a20 = a20.resize((28,28))
        image20 = ImageTk.PhotoImage(a20)

        label20 = tk.Label(cart, image = image20, borderwidth=0, relief='solid')
        label20.place(x=380,y=665)


        l4 = tk.Label(cart, width=700, height=1, bg='#13ab40')
        l4.place(x=0,y=770)

        button3 = tk.Button(cart, text='BACK', font=('inter', 14, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=100, pady=8)
        button3.place(x=70,y=820)
        button4 = tk.Button(cart, text='Proceed To Checkout', font=('inter', 14, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=32, pady=8)
        button4.place(x=370,y=820)

root = tk.Tk()

root.title('Kiosk')
root.geometry('700x900')
root.config(bg='#fab6fa')
root.resizable(width=False, height=False)

pillow_image = Image.open("D:\Documents\IT-Elective\pics\one.png")
pillow_image = pillow_image.resize((700,200))
image = ImageTk.PhotoImage(pillow_image)

label = tk.Label(root, image = image)
label.pack()

button = tk.Button(root, text='Back', font=('inter', 14), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=32, pady=2)
button.pack(side=tk.TOP,anchor=tk.NE, padx=10, pady=10)




a1 = Image.open("D:\Documents\IT-Elective\pics\\two.png")
a1 = a1.resize((145,80))
image1 = ImageTk.PhotoImage(a1)

label1 = tk.Label(root, image = image1, borderwidth=1, relief='solid')
label1.place(x=225,y=260)

a2 = Image.open("D:\Documents\IT-Elective\pics\\three.png")
a2 = a2.resize((140,80))
image2 = ImageTk.PhotoImage(a2)

label2 = tk.Label(root, image = image2, borderwidth=1, relief='solid')
label2.place(x=390,y=260)

a3 = Image.open("D:\Documents\IT-Elective\pics\\four.png")
a3 = a3.resize((140,80))
image3 = ImageTk.PhotoImage(a3)

label3 = tk.Label(root, image = image3, borderwidth=1, relief='solid')
label3.place(x=550,y=260)




a4 = Image.open("D:\Documents\IT-Elective\pics\\5.png")
a4 = a4.resize((140,80))
image4 = ImageTk.PhotoImage(a4)

label4 = tk.Label(root, image = image4, borderwidth=1, relief='solid')
label4.place(x=225,y=360)

a5 = Image.open("D:\Documents\IT-Elective\pics\six.png")
a5 = a5.resize((140,80))
image5 = ImageTk.PhotoImage(a5)

label5 = tk.Label(root, image = image5, borderwidth=1, relief='solid')
label5.place(x=390,y=360)

a6 = Image.open("D:\Documents\IT-Elective\pics\seven.png")
a6 = a6.resize((140,80))
image6 = ImageTk.PhotoImage(a6)

label6 = tk.Label(root, image = image6, borderwidth=1, relief='solid')
label6.place(x=550,y=360)




a7 = Image.open("D:\Documents\IT-Elective\pics\eight.png")
a7 = a7.resize((140,80))
image7 = ImageTk.PhotoImage(a7)

label7 = tk.Label(root, image = image7, borderwidth=1, relief='solid')
label7.place(x=225,y=460)

a8 = Image.open("D:\Documents\IT-Elective\pics\\nine.png")
a8 = a8.resize((140,80))
image8 = ImageTk.PhotoImage(a8)

label8 = tk.Label(root, image = image8, borderwidth=1, relief='solid')
label8.place(x=390,y=460)

a9 = Image.open("D:\Documents\IT-Elective\pics\\ten.png")
a9 = a9.resize((140,80))
image9 = ImageTk.PhotoImage(a9)

label9 = tk.Label(root, image = image9, borderwidth=1, relief='solid')
label9.place(x=550,y=460)






a10 = Image.open("D:\Documents\IT-Elective\pics\eleven.png")
a10 = a10.resize((140,90))
image10 = ImageTk.PhotoImage(a10)

label10 = tk.Label(root, image = image10, borderwidth=1, relief='solid')
label10.place(x=225,y=560)

a11 = Image.open("D:\Documents\IT-Elective\pics\\twelve.png")
a11 = a11.resize((140,90))
image11 = ImageTk.PhotoImage(a11)

label11 = tk.Label(root, image = image11, borderwidth=1, relief='solid')
label11.place(x=390,y=560)

a12 = Image.open("D:\Documents\IT-Elective\pics\\thirteen.png")
a12 = a12.resize((140,90))
image12 = ImageTk.PhotoImage(a12)

label12 = tk.Label(root, image = image12, borderwidth=1, relief='solid')
label12.place(x=550,y=560)




a13 = Image.open("D:\Documents\IT-Elective\pics\\fourtheen.png")
a13 = a13.resize((140,90))
image13 = ImageTk.PhotoImage(a13)

label13 = tk.Label(root, image = image13, borderwidth=1, relief='solid')
label13.place(x=225,y=670)

a14 = Image.open("D:\Documents\IT-Elective\pics\\fiftheen.png")
a14 = a14.resize((140,90))
image14 = ImageTk.PhotoImage(a14)

label14 = tk.Label(root, image = image14, borderwidth=1, relief='solid')
label14.place(x=390,y=670)


a15 = Image.open("D:\Documents\IT-Elective\pics\sixtheen.png")
a15 = a15.resize((140,90))
image15 = ImageTk.PhotoImage(a15)

label15 = tk.Label(root, image = image15, borderwidth=1, relief='solid')
label15.place(x=550,y=670)




meals = tk.Button(root, text='MEALS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
meals.place(x=40,y=275)
appe = tk.Button(root, text='APPETIZERS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
appe.place(x=10,y=375)
drinks = tk.Button(root, text='DRINKS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
drinks.place(x=40,y=475)
desserts = tk.Button(root, text='DESSERTS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
desserts.place(x=25,y=580)
snacks = tk.Button(root, text='SNACKS', borderwidth=2,relief='solid', padx=24,pady=12, font=('Inter', 16, 'bold'), background='WHITE', fg='black', cursor='hand2')
snacks.place(x=40,y=690)

placeorder = tk.Label(root, text='PLACE ORDER - DINE IN', background='#13ab40',font=('Inter', 10, 'bold'), width=700,padx=12,pady=4, anchor='w')
placeorder.place(x=0,y=780)

quantity = tk.Label(root, text='QUANTITY', background='#fab6fa',font=('Inter', 10, 'bold'),)
quantity.place(x=100,y=820)


a17 = Image.open("D:\Documents\IT-Elective\pics\plus.png")
a17 = a17.resize((28,28))
image17 = ImageTk.PhotoImage(a17)

label17 = tk.Label(root, image = image17, borderwidth=0, relief='solid')
label17.place(x=120,y=850)

a18 = Image.open("D:\Documents\IT-Elective\pics\minus.png")
a18 = a18.resize((28,28))
image18 = ImageTk.PhotoImage(a18)

label18 = tk.Label(root, image = image18, borderwidth=0, relief='solid')
label18.place(x=160,y=850)

quantity1 = tk.Label(root, text='01', background='WHITE',font=('Inter', 10, 'bold'), borderwidth=1, relief='solid',padx=12, pady=8)
quantity1.place(x=220,y=845)

button1 = tk.Button(root, text='Cancel order', font=('inter', 14), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=26, pady=8)
button1.place(x=320,y=830)
button2 = tk.Button(root, text='Place order', font=('inter', 14), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=26, pady=8, command= Extra)
button2.place(x=520,y=830)


meal1 = tk.Label(root, text='A-1 Burger with Fries', background='#fab6fa',font=('Inter', 7, 'bold'),)
meal1.place(x=225,y=342)
meal2 = tk.Label(root, text='A-2 Spaghetti with Chicken', background='#fab6fa',font=('Inter', 7, 'bold'),)
meal2.place(x=390,y=342)
meal3 = tk.Label(root, text='A3-2 piece Chicken with Mashed potato', background='#fab6fa',font=('Inter', 7, 'bold'),)
meal3.place(x=548,y=342)

appe1 = tk.Label(root, text='B1-Salad', background='#fab6fa',font=('Inter', 7, 'bold'),)
appe1.place(x=225,y=442)
appe2 = tk.Label(root, text='B2-Chicken with Fries', background='#fab6fa',font=('Inter', 7, 'bold'),)
appe2.place(x=390,y=442)
appe3 = tk.Label(root, text='B3-Bucket of Fries', background='#fab6fa',font=('Inter', 7, 'bold'),)
appe3.place(x=548,y=442)

drink1 = tk.Label(root, text='C1-Coke,Fanta,Sprite,Pepsi', background='#fab6fa',font=('Inter', 7, 'bold'),)
drink1.place(x=225,y=542)
drink2 = tk.Label(root, text='C2-Coke Float', background='#fab6fa',font=('Inter', 7, 'bold'),)
drink2.place(x=390,y=542)
drink3 = tk.Label(root, text='C3-Iced Coffee', background='#fab6fa',font=('Inter', 7, 'bold'),)
drink3.place(x=548,y=542)

dessert1 = tk.Label(root, text='D1-Apple pie', background='#fab6fa',font=('Inter', 7, 'bold'),)
dessert1.place(x=225,y=652)
dessert2 = tk.Label(root, text='D2-Cupcakes', background='#fab6fa',font=('Inter', 7, 'bold'),)
dessert2.place(x=390,y=652)
dessert3 = tk.Label(root, text='D3-Ice Cream', background='#fab6fa',font=('Inter', 7, 'bold'),)
dessert3.place(x=548,y=652)

snack1 = tk.Label(root, text='E1-Hotdot Sandwich', background='#fab6fa',font=('Inter', 7, 'bold'),)
snack1.place(x=225,y=762)
snack2 = tk.Label(root, text='E2-Fries and Nuggets', background='#fab6fa',font=('Inter', 7, 'bold'),)
snack2.place(x=390,y=762)
snack3 = tk.Label(root, text='E3-6 pieces Nuggets with Fries', background='#fab6fa',font=('Inter', 7, 'bold'),)
snack3.place(x=548,y=762)


price1 = tk.Label(root, text='₱129', background='WHITE',font=('Inter', 7, 'bold'),)
price1.place(x=335,y=265)
price2 = tk.Label(root, text='₱159', background='WHITE',font=('Inter', 7, 'bold'),)
price2.place(x=500,y=265)
price3 = tk.Label(root, text='₱201', background='WHITE',font=('Inter', 7, 'bold'),)
price3.place(x=660,y=265)

price4 = tk.Label(root, text='₱150', background='WHITE',font=('Inter', 7, 'bold'),)
price4.place(x=335,y=365)
price5 = tk.Label(root, text='₱130', background='WHITE',font=('Inter', 7, 'bold'),)
price5.place(x=500,y=365)
price6 = tk.Label(root, text='₱105', background='WHITE',font=('Inter', 7, 'bold'),)
price6.place(x=660,y=365)

price7 = tk.Label(root, text='₱90', background='WHITE',font=('Inter', 7, 'bold'),)
price7.place(x=335,y=465)
price8 = tk.Label(root, text='₱109', background='WHITE',font=('Inter', 7, 'bold'),)
price8.place(x=500,y=465)
price8 = tk.Label(root, text='₱115', background='WHITE',font=('Inter', 7, 'bold'),)
price8.place(x=660,y=465)

price9 = tk.Label(root, text='₱130', background='WHITE',font=('Inter', 7, 'bold'),)
price9.place(x=335,y=565)
price10 = tk.Label(root, text='₱100', background='WHITE',font=('Inter', 7, 'bold'),)
price10.place(x=500,y=565)
price11 = tk.Label(root, text='₱50', background='WHITE',font=('Inter', 7, 'bold'),)
price11.place(x=660,y=565)

price12 = tk.Label(root, text='₱112', background='WHITE',font=('Inter', 7, 'bold'),)
price12.place(x=335,y=675)
price13 = tk.Label(root, text='₱145', background='WHITE',font=('Inter', 7, 'bold'),)
price13.place(x=500,y=675)
price14 = tk.Label(root, text='₱120', background='WHITE',font=('Inter', 7, 'bold'),)
price14.place(x=660,y=675)



root.mainloop()