# calculator
from tkinter import *

root = Tk()
root.title('CALCULATOR')

result = Entry(root, width = 42, borderwidth = 5, bg = 'grey', fg = 'white')
result.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 20)

def button_click(number):
    current = result.get()
    result.delete(0, END)
    result.insert(0, str(current) + str(number))

def clear():
    result.delete(0, END)

def equal():
    second_num = result.get()
    result.delete(0, END)
    if math == 'addition':
        result.insert(0, f_num + int(second_num))
    elif math == 'subtraction':
        result.insert(0, f_num - int(second_num))
    elif math == 'multiplication':
        result.insert(0, f_num * int(second_num))
    elif math == 'division':
        result.insert(0, f_num / int(second_num))

def add():
    first_num = result.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_num)
    result.delete(0, END)

def subtract():
    first_num = result.get()
    global f_num
    global math
    math = 'subtraction'
    f_num = int(first_num)
    result.delete(0, END)

def multiply():
    first_num = result.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_num)
    result.delete(0, END)

def divide():
    first_num = result.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_num)
    result.delete(0, END)

# create buttons
n1 = Button(root, text = '1', padx = 30, pady = 20, command = lambda: button_click(1), bg = 'grey', fg = 'white')
n2 = Button(root, text = '2', padx = 30, pady = 20, command = lambda: button_click(2), bg = 'grey', fg = 'white')
n3 = Button(root, text = '3', padx = 30, pady = 20, command = lambda: button_click(3), bg = 'grey', fg = 'white')
n4 = Button(root, text = '4', padx = 30, pady = 20, command = lambda: button_click(4), bg = 'grey', fg = 'white')
n5 = Button(root, text = '5', padx = 30, pady = 20, command = lambda: button_click(5), bg = 'grey', fg = 'white')
n6 = Button(root, text = '6', padx = 30, pady = 20, command = lambda: button_click(6), bg = 'grey', fg = 'white')
n7 = Button(root, text = '7', padx = 30, pady = 20, command = lambda: button_click(7), bg = 'grey', fg = 'white')
n8 = Button(root, text = '8', padx = 30, pady = 20, command = lambda: button_click(8), bg = 'grey', fg = 'white')
n9 = Button(root, text = '9', padx = 30, pady = 20, command = lambda: button_click(9), bg = 'grey', fg = 'white')
n0 = Button(root, text = '0', padx = 30, pady = 20, command = lambda: button_click(0), bg = 'grey', fg = 'white')
button_add = Button(root, text = '+', padx = 29, pady = 20, command = add, bg = 'grey', fg = 'white')
button_sub = Button(root, text = '-', padx = 30, pady = 20, command = subtract, bg = 'grey', fg = 'white')
button_equal = Button(root, text = '=', padx = 29, pady = 20, command = equal, bg = 'grey', fg = 'white')
button_clear = Button(root, text = 'C', padx = 29, pady = 20, command = clear, bg = 'grey', fg = 'white')
button_mul = Button(root, text = '*', padx = 30, pady = 20, command = multiply, bg = 'grey', fg = 'white')
button_div = Button(root, text = '/', padx = 30, pady = 20, command = divide, bg = 'grey', fg = 'white')

# put the buttons on the screen
n1.grid(row = 1, column = 0)
n2.grid(row = 1, column = 1)
n3.grid(row = 1, column = 2)
n4.grid(row = 2, column = 0)
n5.grid(row = 2, column = 1)
n6.grid(row = 2, column = 2)
n7.grid(row = 3, column = 0)
n8.grid(row = 3, column = 1)
n9.grid(row = 3, column = 2)
n0.grid(row = 4, column = 1)
button_add.grid(row = 2, column = 3)
button_sub.grid(row = 1, column = 3)
button_equal.grid(row = 4, column = 2)
button_clear.grid(row = 4, column = 0)
button_mul.grid(row = 3, column = 3)
button_div.grid(row = 4, column = 3)

root.mainloop()