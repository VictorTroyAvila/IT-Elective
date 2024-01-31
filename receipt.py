import tkinter as tk

def back():
    root.destroy()
    import kiosk

root = tk.Tk()
root.title('Kiosk')
root.geometry('700x900')
root.config(bg='#fab6fa')
root.resizable(width=False, height=False)

frame1 = tk.Frame(root, width=450, height=1500, bg='WHITE', borderwidth=2, relief='solid')
frame1.pack(padx=20, pady=20)

text_receipt = [
    "",
    "",
    "----------------------------------------------------------------------------------------------------------------",
    "Your order number is",
    "183",
    "----------------------------------------------------------------------------------------------------------------",
    "Welcome to Very Fast Food",
    "Restaurant Number #1456237429395",
    " TAX INVOICE",
    " KS#1                     14/01/2024       02:23:57 PM",
    " QTY ITEM                                          TOTAL",
    " 1                      Burger With Fries        129.00",
    " 1                      2 piece Chicken          109.00",
    "",
    "",
    "",
    "Subtotal                               238.00",
    "Take-Out Total                          00.00",
    "Money Received                         500.00",
    "Change                                 262.00",
    "",
    "",
    "*Indicates tax-free items",
    "",
    "",
    "",
    "",
    "",
    "THANK YOU COME AGAIN!!!!!!!!",
    "",
    "",
    "",
    "",
]

for item in text_receipt:
    if "Your order number is" in item or item.isdigit():
        receipt_label = tk.Label(frame1, text=item, font=("Inter", 20, "bold"), bg='WHITE', fg='black')
    elif any(field in item for field in ["Subtotal","Take-Out Total","Money Received","Change"]):
        receipt_label = tk.Label(frame1, text=item.ljust(50), font=("Courier", 12, "normal"), bg='WHITE')
    else:
        receipt_label = tk.Label(frame1, text=item, font=("Arial", 12, "normal"), bg='WHITE')
    receipt_label.pack()

root.after(10000, back)
root.mainloop()