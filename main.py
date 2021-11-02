'''
Andy Walsh
GUIS
Oct. 12
'''

from tkinter import *
from tkinter import messagebox

#tkinter name for instance
root = Tk()

#setting the window size
root.geometry("900x500")
root.configure(bg= 'grey')

#creating a label for
box_1_label = Label(root, text='user-input-1', font=('calibre', 10,'bold'))
#this places the label
box_1_label.grid(row=0, column=0)

box_2_label = Label(root, text='user-input-2', font=('calibre', 10,'bold'))
#this places the label
box_2_label.grid(row=1, column=0)

box_3_label = Label(root, text='Sliders:', font=('calibre', 10,'bold'))
#this places the label
box_3_label.grid(row=8, column=7)

box_4_label = Label(root, text='Select Code:', font=('calibre', 10,'bold'))
#this places the label
box_4_label.grid(row=15, column=0)

def pop_up():
    messagebox.showwarning("showwarning", "WARNING... Self distruct process has begun...")

#buttons
pop_up_btn = Button(root, text='pop up', command=pop_up)
pop_up_btn.grid(row=0, column=2)
#performing an infinite loop
#for window display

def radio_1():
    print("radio 1")
def radio_2():
    print("Radio 2")
def radio_3():
    print("Radio 3")
def radio_4():
    print("Radio 4")
def radio_5():
    print("Radio 5")
def radio_6():
    print("Radio 6")

#radio buttons

r= IntVar()

R1 = Radiobutton(root, text='Option 1', value=0, variable=r, command=radio_1)
R1.grid(row=10, column=1)
R2 = Radiobutton(root, text='Option 2', value=1, variable=r, command=radio_2)
R2.grid(row=10, column=2)

a = IntVar()
R3 = Radiobutton(root, text='Option 3', value=0, variable=a, command=radio_3)
R3.grid(row=11, column=3)
R4 = Radiobutton(root, text='Option 4', value=1, variable=a, command=radio_4)
R4.grid(row=11, column=4)

v= IntVar()
R5 = Radiobutton(root, text='Option 5', value=0, variable= v, command=radio_5)
R5.grid(row=12, column=5)
R6 = Radiobutton(root, text='Option 6', value=1, variable= v, command=radio_6)
R6.grid(row=12, column=6)

clicked = StringVar()
main_menu = OptionMenu(root, clicked, "C++","Java","Python","Rust","Go","Ruby")
main_menu.grid(row=16, column=0)

#Slider
slider_1 = Scale(root, from_=0, to=100, orient=HORIZONTAL)
slider_1.grid(row=9, column=7)
slider_2 = Scale(root, from_=0, to=1000, orient=HORIZONTAL)
slider_2.grid(row=10, column=7)

#spin box
spin_box_1 = Spinbox(root, from_=0, to=20)
spin_box_1.grid(row=0, column=8)
#root.mainloop()

#text entry
entry_box_1 = Entry(root, font=('calibre', 10, 'normal'))
entry_box_1.grid(row=8, column=8)

#Check Boxes:

def test_fun():
    print('test_fun')
check_box_1 = Checkbutton(root, text='Option 1', onvalue=1, offvalue=0, command=test_fun)
check_box_1.grid(row=15, column=7)
check_box_2 = Checkbutton(root, text='Option 2', onvalue=1, offvalue=0, command=test_fun)
check_box_2.grid(row=16, column=7)
check_box_3 = Checkbutton(root, text='Option 3', onvalue=1, offvalue=0, command=test_fun)
check_box_3.grid(row=17, column=7)
check_box_4 = Checkbutton(root, text='Option 4', onvalue=1, offvalue=0, command=test_fun)
check_box_4.grid(row=18, column=7)


root.mainloop()