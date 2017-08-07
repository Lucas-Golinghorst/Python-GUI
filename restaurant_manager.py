from Tkinter import *
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

text_input = StringVar()

top_frame = Frame(root, width=1600, bg="green", relief=SUNKEN)
top_frame.pack(side=TOP)

left_frame = Frame(root, width=800, height=700, bg="green", relief=SUNKEN)
left_frame.pack(side=LEFT)

right_frame = Frame(root, width=300, height=700, bg="green", relief=SUNKEN)
right_frame.pack(side=RIGHT)

#Stores current time
current_time = time.asctime(time.localtime(time.time()))


#GUI NAME DISPLAY
title_name = Label(top_frame, font=('arial', 50, 'bold'), text="Restaurant Management System", fg="Black", bd=10, anchor='w')
title_name.grid(row=0, column=0)
title_name = Label(top_frame, font=('arial', 18, 'bold'), text=current_time, fg="Black", bd=10, anchor='w')
title_name.grid(row=1, column=0)

#CALCULATOR
text_display = Entry(right_frame, font=('arial', 18, 'bold'), textvariable=text_input, bd=30, insertwidth=4,
                     bg="green", justify='right')
text_display.grid(columnspan=4)

root.mainloop()
