import tkinter as tk
from tkinter import ttk

class Calculator():
    def window(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        width = 400
        height = 400
        display_width = self.root.winfo_screenwidth()
        display_height = self.root.winfo_screenheight()
        left = int(display_width/2 - width/2)
        top = int(display_height/2 - height/2)
        self.root.geometry(f'{width}x{height}+{left}+{top}')
        self.root.resizable(False, False)

    def display(self):
        self.display = tk.StringVar()
        display_entry = ttk.Entry(self.root, textvariable=self.display, font=('Arial 60 bold'), justify='right',state='disabled')
        display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

    def buttons(self):
        buttons = [
            '7','8','9','/',
            '4','5','6','*',
            '1','2','3','-',
            '0','AC','=','+',
        ]

        button_style = ttk.Style()
        button_style.configure('TButton', font=('Arial', 25))

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(self.root, text=button, style="TButton", command=lambda b=button: self.on_button_click(b)).grid(
                row=row_val, column=col_val, padx=10, pady=5, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        for i in range(4):
            self.root.columnconfigure(i, weight=1)
        for i in range(1, 6):
            self.root.rowconfigure(i, weight=1)

    def on_button_click(self, button):
        current_text = self.display.get()

        if button == 'AC':
            self.display.set('')
        elif button == '=':
            try:
                result = eval(current_text)
                self.display.set(result)
            except Exception as e:
                self.display.set('')
        else:
            self.display.set(current_text + button)

    def run(self):
        self.window()
        self.display()
        self.buttons()
        self.root.mainloop()

calculator = Calculator()
calculator.run()