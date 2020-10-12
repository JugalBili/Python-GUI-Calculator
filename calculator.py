# -*- coding: utf-8 -*-
""" Simple GUI Calculator Program """

from tkinter import *
root = Tk()
#root.geometry("450x500")]

frame_1 = Frame(root)
frame_1.pack()
frame_2 = Frame(root)
frame_2.pack()

Label(frame_1, pady = 1).pack()
my_entry = Entry(frame_1, width = 51, borderwidth = 5, justify = RIGHT)
my_entry.pack()
display_label = Label(frame_1, width = 40, anchor = E)
display_label.pack()
Label(frame_1, pady = 1).pack()

number_array = []
operations_array = []
temp_string = ""

def update_label():
   
    global temp_string 
    temp_string = ""
    
    for i in range(len(number_array)):
        temp_string = temp_string+str(number_array[i])+str(operations_array[i])
    
    display_label["text"] = temp_string

def button_click(num):
    my_entry.insert(END,num)

def button_add():
    number_array.append(int(my_entry.get()))
    operations_array.append("+")
    my_entry.delete(0,END)
    update_label()

def button_sub():
    number_array.append(int(my_entry.get()))
    operations_array.append("-")
    my_entry.delete(0,END)
    update_label()
    
def button_mul():
    number_array.append(int(my_entry.get()))
    operations_array.append("x")
    my_entry.delete(0,END)
    update_label()

def button_div():
    number_array.append(int(my_entry.get()))
    operations_array.append("÷")
    my_entry.delete(0,END)
    update_label()

def button_clear():
    my_entry.delete(0,END)
    number_array.clear()
    operations_array.clear()
    tempString = ""
    update_label()

def button_equal():
    number_array.append(int(my_entry.get()))
    operations_array.append("")
    my_entry.delete(0,END)
    update_label()
    
    temp_num = number_array
    temp_operations = operations_array
    temp_operations.pop()
    
    for j in range(len(temp_num)):
        #print(temp_num)
        #print(temp_operations)
        #checking for multiplications 
        for i in range(len(temp_num)-1):
            try:
                if (temp_operations[i] == 'x') and (i-1 == -1):
                    temp_num[i] = temp_num[i]*temp_num[i+1]
                    temp_num.pop(i+1)
                    temp_operations.pop(i)
                
                if (temp_operations[i] == 'x') and (temp_operations[i-1] == "÷"):
                    pass
                
                elif (temp_operations[i] == 'x'):
                    temp_num[i] = temp_num[i]*temp_num[i+1]
                    temp_num.pop(i+1)
                    temp_operations.pop(i)
            
            except IndexError:
                continue
            
        #checking for divisions
        for i in range(len(temp_num)-1):
            try: 
                if (temp_operations[i] == '÷') and (i-1 == -1):
                    temp_num[i] = temp_num[i]/temp_num[i+1]
                    temp_num.pop(i+1)
                    temp_operations.pop(i)
                
                if (temp_operations[i] == '÷') and (temp_operations[i-1] == "x"):
                    pass
                
                elif (temp_operations[i] == '÷'):
                    temp_num[i] = temp_num[i]/temp_num[i+1]
                    temp_num.pop(i+1)
                    temp_operations.pop(i)
                
            except IndexError:
                continue

            except ZeroDivisionError:
                display_label["text"] = "Error! Division by 0"
            
        #checking for subtractions
        for i in range(len(temp_num)-1):
            #print(i)
            #print(temp_num)
            #print(temp_operations)
            try:
                if (temp_operations[i] == '-') and (i-1 == -1):
                    temp_num[i] = temp_num[i]-temp_num[i+1]
                    temp_num.pop(i+1)
                    temp_operations.pop(i)
                
                if (temp_operations[i] == '-') and (temp_operations[i-1] == "+"):
                    pass
                
                elif (temp_operations[i] == '-'):
                    temp_num[i] = temp_num[i]-temp_num[i+1]
                    temp_num.pop(i+1)
                    temp_operations.pop(i)
                    
            except IndexError:
                continue
                
        #checking for addition
        for i in range(len(temp_num)-1):
            #print(i)
            #print(temp_num)
            #print(temp_operations)
            try:
                if (temp_operations[i] == '+') and (i-1 == -1):
                    temp_num[i] = temp_num[i]+temp_num[i+1]
                    temp_num.pop(i+1)
                    temp_operations.pop(i)
                
                if (temp_operations[i] == '+') and (temp_operations[i-1] == "-"):
                    pass
                
                elif (temp_operations[i] == '+'):
                    temp_num[i] = temp_num[i]+temp_num[i+1]
                    temp_num.pop(i+1)
                    temp_operations.pop(i)
                    
            except IndexError:
                continue
            
    my_entry.insert(0,temp_num[0]) 


def button_del():
    length = len(my_entry.get())
    my_entry.delete(length-1,END)

# initializing button widgets
button_1 = Button(frame_2, text = "1", padx = 30, pady = 20, command = lambda: button_click(1))
button_2 = Button(frame_2, text = "2", padx = 30, pady = 20, command = lambda: button_click(2))
button_3 = Button(frame_2, text = "3", padx = 30, pady = 20, command = lambda: button_click(3))
button_4 = Button(frame_2, text = "4", padx = 30, pady = 20, command = lambda: button_click(4))
button_5 = Button(frame_2, text = "5", padx = 30, pady = 20, command = lambda: button_click(5))
button_6 = Button(frame_2, text = "6", padx = 30, pady = 20, command = lambda: button_click(6))
button_7 = Button(frame_2, text = "7", padx = 30, pady = 20, command = lambda: button_click(7))
button_8 = Button(frame_2, text = "8", padx = 30, pady = 20, command = lambda: button_click(8))
button_9 = Button(frame_2, text = "9", padx = 30, pady = 20, command = lambda: button_click(9))
button_0 = Button(frame_2, text = "0", padx = 30, pady = 20, command = lambda: button_click(0))

button_add = Button(frame_2, text = "+", padx = 29, pady = 20, command = button_add)
button_sub = Button(frame_2, text = "-", padx = 30, pady = 20, command = button_sub)
button_mul = Button(frame_2, text = "x", padx = 30, pady = 20, command = button_mul)
button_div = Button(frame_2, text = "÷", padx = 30, pady = 20, command = button_div)

button_clear = Button(frame_2, text = "Clear", padx = 60, pady = 20, command = button_clear)
button_del = Button(frame_2, text = "Del", padx = 25, pady = 20, command = button_del)
button_equal = Button(frame_2, text = "=", padx = 70, pady = 20, command = button_equal)


# adding buttons to screen 
button_7.grid(row = 0, column = 0)
Label(frame_2, padx = 0.2).grid(row = 0, column = 1)
button_8.grid(row = 0, column = 2)
Label(frame_2, padx = 0.2).grid(row = 0, column = 3)
button_9.grid(row = 0, column = 4)
Label(frame_2, padx = 0.2).grid(row = 0, column = 5)
button_add.grid(row = 0, column = 6)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 2)
button_6.grid(row = 2, column = 4)
button_sub.grid(row = 2, column = 6)

button_1.grid(row = 4, column = 0)
button_2.grid(row = 4, column = 2)
button_3.grid(row = 4, column = 4)
button_mul.grid(row = 4, column = 6)

button_0.grid(row = 6, column = 0)
button_clear.grid(row = 6, column = 2, columnspan = 3) # 'columnspan' allows widget to use stated number of columns instead of 1
button_div.grid(row = 6, column = 6)


button_equal.grid(row = 8, column = 2, columnspan = 3)
button_del.grid(row = 8, column = 6)


root.mainloop()

