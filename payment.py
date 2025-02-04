import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

def receipt():
    root.destroy()
    import receipt

root = tk.Tk()

root.title('Payment')
root.geometry('700x900')
root.config(bg='#fab6fa')
root.resizable(width=False, height=False)

image_path = "D:\Documents\IT-Elective\pics\qr.jpg"
original_image = Image.open(image_path)

new_width = 500
new_height = 600
resized_image = original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)

photo = ImageTk.PhotoImage(resized_image)

image_label = tk.Label(root, image=photo, bg='#fab6fa')
image_label.place(x=100, y=100)

line = tk.Label(root, background='#13ab40', width=700, padx=12, pady=4, anchor='w')
line.place(x=0, y=780)

button3 = tk.Button(root, text='Proceed', font=('inter', 14, 'bold'), background='#13ab40', fg='white', cursor='hand2',borderwidth=0, padx=100, pady=8, command= receipt)
button3.place(x=200,y=820)

root.mainloop()