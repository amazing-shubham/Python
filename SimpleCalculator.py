from tkinter import *
import parser
root = Tk()
root.title("Calculator")
# adding display
displayScreen=Entry(root)
displayScreen.grid(row=0, columnspan=8, sticky=W+E)

# logic to display the presses button
i = 0
def display (num):
    global i
    displayScreen.insert(i, num)
    i = i+1

# logic for Clear All Button
def clearAll():
    displayScreen.delete(0, END)

# logic for deleting one by one
def delete():
    display_string = displayScreen.get()
    if len(display_string):
        newString=display_string[:-1]
        clearAll()
        displayScreen.insert(0,newString)
    else:
        clearAll()
        displayScreen.insert(0, "0")

# logic to display the operator
def get_Operator(operator):
    global i
    x=len(operator)
    displayScreen.insert(i, operator)
    i=i+x

# logic to calculate
def calculate():
    display_string=displayScreen.get()
    try:
        a = parser.expr(display_string).compile()
        output = eval(a)
        clearAll()
        displayScreen.insert(0, output)
    except Exception:
        clearAll()
        displayScreen.insert(0, "ERROR")


# logic to calculate factorial
def factorial():
    whole_string = displayScreen.get()
    num = int(whole_string)
    fact = 1
    try:
        if num==0:
            clearAll()
            displayScreen.insert(0,"1")
        else:
            while num>0:
                fact = fact*num
                num = num-1
                clearAll()
                displayScreen.insert(0, fact)
    except Exception:
        clearAll()
        displayScreen.insert(0,"Error")


# adding number button
Button(root, text='1', command=lambda :display(1)).grid(row=1, column=0)
Button(root, text='2', command=lambda :display(2)).grid(row=1, column=1)
Button(root, text='3', command=lambda :display(3)).grid(row=1, column=2)

Button(root, text='4', command=lambda :display(4)).grid(row=2, column=0)
Button(root, text='5', command=lambda :display(5)).grid(row=2, column=1)
Button(root, text='6', command=lambda :display(6)).grid(row=2, column=2)

Button(root, text='7', command=lambda :display(7)).grid(row=3, column=0)
Button(root, text='8', command=lambda :display(8)).grid(row=3, column=1)
Button(root, text='9', command=lambda :display(9)).grid(row=3, column=2)

Button(root, text='AC',command=lambda : clearAll()).grid(row=4, column=0)
Button(root, text='0', command=lambda :display(0)).grid(row=4, column=1)
Button(root, text='=', command=lambda : calculate()).grid(row=4, column=2)

# adding operator buttons
Button(root, text='+', command=lambda: get_Operator("+")).grid(row=1, column=4)
Button(root, text='-', command=lambda: get_Operator("-")).grid(row=2, column=4)
Button(root, text='*', command=lambda: get_Operator("*")).grid(row=3, column=4)
Button(root, text='/', command=lambda: get_Operator("/")).grid(row=4, column=4)

Button(root, text='pi', command=lambda: get_Operator("*3.14")).grid(row=1, column=5)
Button(root, text='%', command=lambda: get_Operator("%")).grid(row=2, column=5)
Button(root, text='(', command=lambda: get_Operator("(")).grid(row=3, column=5)
Button(root, text='exp', command=lambda: get_Operator("**")).grid(row=4, column=5)

Button(root, text='<-', command=lambda :delete()).grid(row=1, column=6)
Button(root, text='x!', command=lambda : factorial()).grid(row=2, column=6)
Button(root, text=')', command=lambda: get_Operator(")")).grid(row=3, column=6)
Button(root, text='^2', command=lambda: get_Operator("**2")).grid(row=4, column=6)

root.mainloop()
