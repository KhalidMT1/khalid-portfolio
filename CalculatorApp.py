from tkinter import *
from tkinter import ttk

class Calculator:
    calc_value = 0.0
    div_trigger = False
    mult_trigger = False
    add_trigger = False
    sub_trigger = False

    def button_press(self, value):

        if value == 'AC':
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.number_entry.delete(0, "end")#delete from 0 index to end


        else:
            entry_val = self.number_entry.get()
            entry_val += value #put the new value to the right of it, everything is considered string still
            self.number_entry.delete(0, "end")#delete from 0 index to end
            self.number_entry.insert(0, entry_val)#insert my new value

    def is_float(self, str_val):
        try:
            float(str_val)
            return True #it's never going to get to this true statement if an exception occurs
        except ValueError:
            return False

    def math_button_press(self, value):
        if self.is_float(str(self.number_entry.get())):
            self.div_trigger = False
            self.mult_trigger = False
            self.add_trigger = False
            self.sub_trigger = False
            self.calc_value = float(self.entry_value.get())
            if value == "/":
                self.div_trigger = True
            elif value == "*":
                self.mult_trigger = True
            elif value == "+":
                self.add_trigger = True
            else:
                self.sub_trigger = True

            self.number_entry.delete(0, "end")

    def equal_button_press(self):
        if self.add_trigger or self.sub_trigger or self.mult_trigger or self.div_trigger:
            if self.add_trigger:
                solution = self.calc_value + float(self.entry_value.get())
            elif self.sub_trigger:
                solution = self.calc_value - float(self.entry_value.get())
            elif self.mult_trigger:
                solution = self.calc_value * float(self.entry_value.get())
            else:
                solution = self.calc_value / float(self.entry_value.get())

            self.number_entry.delete(0, "end")
            self.number_entry.insert(0, solution)

    def __init__(self, root):
        self.entry_value = StringVar(root, value='')
        root.title("Calculator")
        root.geometry("600x250")
        root.resizable(width=False, height=False)
        style = ttk.Style()
        style.configure("TButton", font="Serif 15", padding=10)
        style.configure("TEntry", font="Serif 18", padding=10)
        self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=50)
        self.number_entry.grid(row=0, columnspan=4, sticky=(W, E))

        self.button7 = ttk.Button(root, text="7", command=lambda:
        self.button_press('7')).grid(row=1, column=0, sticky=(W, E))
        self.button8 = ttk.Button(root, text="8", command=lambda:
        self.button_press('8')).grid(row=1, column=1, sticky=(W, E))
        self.button9 = ttk.Button(root, text="9", command=lambda:
        self.button_press('9')).grid(row=1, column=2, sticky=(W, E))
        self.button_div = ttk.Button(root, text="/", command=lambda:
        self.math_button_press('/')).grid(row=1, column=3, sticky=(W, E))

        self.button4 = ttk.Button(root, text="4", command=lambda:
        self.button_press('4')).grid(row=2, column=0, sticky=(W, E))
        self.button5 = ttk.Button(root, text="5", command=lambda:
        self.button_press('5')).grid(row=2, column=1, sticky=(W, E))
        self.button6 = ttk.Button(root, text="6", command=lambda:
        self.button_press('6')).grid(row=2, column=2, sticky=(W, E))
        self.button_mult = ttk.Button(root, text="*", command=lambda:
        self.math_button_press('*')).grid(row=2, column=3, sticky=(W, E))

        self.button1 = ttk.Button(root, text="1", command=lambda:
        self.button_press('1')).grid(row=3, column=0, sticky=(W, E))
        self.button2 = ttk.Button(root, text="2", command=lambda:
        self.button_press('2')).grid(row=3, column=1, sticky=(W, E))
        self.button3 = ttk.Button(root, text="3", command=lambda:
        self.button_press('3')).grid(row=3, column=2, sticky=(W, E))
        self.button_add= ttk.Button(root, text="+", command=lambda:
        self.math_button_press('+')).grid(row=3, column=3, sticky=(W, E))

        self.button_clear = ttk.Button(root, text="AC", command=lambda:
        self.button_press('AC')).grid(row=4, column=0, sticky=(W, E))
        self.button0 = ttk.Button(root, text="0", command=lambda:
        self.button_press('0')).grid(row=4, column=1, sticky=(W, E))
        self.button_equal = ttk.Button(root, text="=", command=lambda:
        self.equal_button_press()).grid(row=4, column=2, sticky=(W, E))
        self.button_sub = ttk.Button(root, text="-", command=lambda:
        self.math_button_press('-')).grid(row=4, column=3, sticky=(W, E))


root = Tk()
calc = Calculator(root)
root.mainloop()