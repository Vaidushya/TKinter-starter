from tkinter import *

# window
root = Tk()
root.title("Getting Started With Widgets")
root.geometry("500x500")
root.configure(bg="#333333")

# add widgets
# labels
lbl0 = Label(text="Multiplication of Two Numbers", fg="#ff3399", bg="#333333", font=("Arial", 20), pady=10)
lbl1 = Label(text="First number", bg="#333333", fg="white", font=("Arial", 12))
lbl2 = Label(text="Second number", bg="#333333", fg="white", font=("Arial", 12))
lbl3 = Label(text="Result", bg="#333333", fg="white", font=("Arial", 12))

# entry widgets
num1_entry = Entry(font=("Arial", 12))
num2_entry = Entry(font=("Arial", 12))

# function to calculate product
def product():
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())
        result = num1 * num2
        result_area.delete("1.0", END) 
        result_area.insert(END, str(result))
    except ValueError:
        result_area.delete("1.0", END)
        result_area.insert(END, "Invalid Input")

# result display area
result_area = Text(bg="#ffffff", fg="black", height=1, width=20, font=("Arial", 12))

# button inside a frame
frame = Frame(root, bg='#333333')
btn = Button(frame, text="Calculate Product", command=product, bg="#ff3399", fg="white", font=("Arial", 12), padx=10, pady=5)

# placing widgets
lbl0.pack()
lbl1.pack()
num1_entry.pack()
lbl2.pack()
num2_entry.pack()
lbl3.pack()
result_area.pack()
frame.pack(pady=20)
btn.pack()
frame.pack()

# start the GUI event loop
root.mainloop()