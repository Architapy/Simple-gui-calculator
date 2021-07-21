# Python program to create simple GUI calculator
# calculator using tkinter

# importing tkinter module
from  tkinter import *

# globally declaring the expression varibale
expression = ""

# Function to update expression in the text entry box
def press(num):
# point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
# Try and except statement is used for handling the errors like zero division error etc.
# Put that code inside the try block which may generate the error.
    try:
        global expression
        # eval function evaluate the expression and str function convert the result into string
        total = str(eval(expression))
        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""


    # if error is generate then handle
    # by the except block
    except:
        equation.set("error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# driver code
if __name__ == '__main__':
    # create a gui window
    root = Tk()

    # set background to gui window
    root.configure(background = "black")

    # set height and width of the window
    root.geometry("240x200")

    # icon of calculator
    root.wm_iconbitmap("calculator.ico")

    # title of the window
    root.title("Python simple GUI calculator using tkinter")

    # stringvar() is the variable class, we create an instance of this class
    equation = StringVar()

    # create the text entry box for showing the expression
    expression_field = Entry(root, textvar = equation)

    # grid method is used for placing the widgets at respective positions in table like structure.
    expression_field.grid(columnspan = 10, ipadx = 140)

    # create a Buttons and place at a particular location inside the root window. when user press the button, the command or
    # function affiliated to that button is executed
    button1 = Button(root, text=' 1 ', fg='black', bg='Light blue',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(root, text=' 2 ', fg='black', bg='Light blue',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(root, text=' 3 ', fg='black', bg='Light blue',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(root, text=' 4 ', fg='black', bg='Light blue',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(root, text=' 5 ', fg='black', bg='Light blue',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(root, text=' 6 ', fg='black', bg='Light blue',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(root, text=' 7 ', fg='black', bg='Light blue',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(root, text=' 8 ', fg='black', bg='Light blue',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(root, text=' 9 ', fg='black', bg='Light blue',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(root, text=' C', fg='black', bg='Light blue',
                     command=clear, height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(root, text=' = ', fg='black', bg='Light blue',
                  command=equalpress, height=1, width=7)
    plus.grid(row=6, column=1)

    minus = Button(root, text=' - ', fg='black', bg='Light blue',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=6, column=2)

    multiply = Button(root, text=' * ', fg='black', bg='Light blue',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=7, column=0)

    divide = Button(root, text=' / ', fg='black', bg='Light blue',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=7, column=2)

    equal = Button(root, text=' . ', fg='black', bg='Light blue',
                   command=lambda: press("."), height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(root, text='0', fg='black', bg='Light blue',
                   command= lambda: press(0), height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal = Button(root, text='+', fg='black', bg='Light blue',
                     command=lambda: press('+'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    percentage = Button(root, text = '%', fg= 'black', bg = 'Light blue',
                        command = lambda: press('%'), height = 1, width = 7)
    percentage.grid(row = 7, column = 1)
    # start the GUI
    root.mainloop()