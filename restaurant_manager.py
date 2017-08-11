from Tkinter import *
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

text_input = StringVar()
op = ""

top_frame = Frame(root, width=1600, bg="blue", relief=SUNKEN)
top_frame.pack(side=TOP)

left_frame = Frame(root, width=800, height=700, bg="blue", relief=SUNKEN)
left_frame.pack(side=LEFT)

right_frame = Frame(root, width=300, height=700, bg="blue", relief=SUNKEN)
right_frame.pack(side=RIGHT)

# Stores current time
current_time = time.asctime(time.localtime(time.time()))

# GUI NAME DISPLAY
title_name = Label(top_frame, font=('arial', 50, 'bold'), text="Restaurant Management System", fg="Black", bd=10,
                   anchor='w')
title_name.grid(row=0, column=0)
title_name = Label(top_frame, font=('arial', 18, 'bold'), text=current_time, fg="Black", bd=10, anchor='w')
title_name.grid(row=1, column=0)


# CALCULATOR

def btnClick(num):
    global op
    op = op + str(num)
    text_input.set(op)


def clrDisplay():
    global op
    op = ""
    text_input.set(op)


def btnEquals():
    global op
    sumUp = str(eval(op))
    text_input.set(sumUp)
    op = ""


text_display = Entry(right_frame, font=('arial', 18, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                     bg="blue", justify='right')

text_display.grid(columnspan=4)

button_eq = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                   text="=", bg="blue", command=btnEquals).grid(row=5, column=2)

button_div = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                    text="/", bg="blue", command=lambda: btnClick("/")).grid(row=5, column=3)

button_mult = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                     text="*", bg="blue", command=lambda: btnClick("*")).grid(row=4, column=3)

button_add = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                    text="+", bg="blue", command=lambda: btnClick("+")).grid(row=2, column=3)

button_minus = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="-", bg="blue", command=lambda: btnClick("-")).grid(row=3, column=3)

button_clear = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                      text="c", bg="blue", command=clrDisplay).grid(row=5, column=1)

button0 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="0", bg="blue", command=lambda: btnClick(0)).grid(row=5, column=0)

button1 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="1", bg="blue", command=lambda: btnClick(1)).grid(row=4, column=0)

button2 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="2", bg="blue", command=lambda: btnClick(2)).grid(row=4, column=1)

button3 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="3", bg="blue", command=lambda: btnClick(3)).grid(row=4, column=2)

button4 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="4", bg="blue", command=lambda: btnClick(7)).grid(row=3, column=0)

button5 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="5", bg="blue", command=lambda: btnClick(7)).grid(row=3, column=1)

button6 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="6", bg="blue", command=lambda: btnClick(7)).grid(row=3, column=2)

button7 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="7", bg="blue", command=lambda: btnClick(7)).grid(row=2, column=0)

button8 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="8", bg="blue", command=lambda: btnClick(8)).grid(row=2, column=1)

button9 = Button(right_frame, padx=16, pady=16, bd=8, fg="black", font=('arial', 20, 'bold'),
                 text="9", bg="blue", command=lambda: btnClick(9)).grid(row=2, column=2)

root.mainloop()
