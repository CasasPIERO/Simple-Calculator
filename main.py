import tkinter as tk
from tkinter import filedialog, messagebox

class Calculator():

    def __init__(self, root):

        self.root = root
        self.root.title("Simple Calculator")
        self.root.resizable(False, False)
        #self.root.geometry("300x300")

        self.entry = tk.Entry(self.root, bg="#6495DE", bd=15, font=("Arial", 18), insertwidth=1, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

        self.total=0
        self.current=''
        self.tipo_oper=''
        self.retry_oper = True

        buttons = [
            "9", "8", "7", "*",
            "6", "5", "4", "/",
            "3", "2", "1", "+",
            "C", "0", ".", "-",
            "="
        ]

        row = 1
        col = 0

        for button in buttons:
            self.set_buttons(button, row, col)
            col+=1
            if col == 4:
                row +=1
                col = 0

        self.root.bind("<KeyPress>", self.key_pressed)

    def key_pressed(self, event):

        key = event.char

        if key == "\r":
            self.calculate()
            return
        elif key == "\x88":
            self.clear_field()
            return
        elif key == "\x1b":
            self.root.quit()
            return

        self.click(key)

    def clear_field(self):

        self.entry.delete("0", tk.END)
        self.total=0
        self.current=''
        self.tipo_oper=''
        self.retry_oper = False

    def calculate(self):

        if self.tipo_oper == "+":
            self.total += float(self.current)
        elif self.tipo_oper == "-":
            self.total -= float(self.current)
        elif self.tipo_oper == "/":
            self.total /= float(self.current)
        elif self.tipo_oper == "*":
            self.total *= float(self.current)

        self.entry.delete("0", tk.END)
        self.entry.insert("0", round(self.total, 2))

    def click(self, button):

        if (not button in [str(x) for x in range(10)]) and (not button == "."): #Se ha digitado alguna operacion "+", "-", "/" o "*"
            if self.retry_oper:
                self.total = float(self.current)
            self.tipo_oper = button
            self.current = ''
            self.retry_oper = False
        else:
            self.current += button

        self.entry.insert(tk.END, button)

    def set_buttons(self, button, row, col):

        if button == "C":
            b = tk.Button(self.root, text=button, width=5, command=self.clear_field)

        elif button == "=":
            b = tk.Button(self.root, text=button, width=5, command=self.calculate)

        else:
            b = tk.Button(self.root, text=button, width=5, command=lambda: self.click(button))

        b.grid(row=row, column=col)

root = tk.Tk()
my_gui = Calculator(root)
root.mainloop()