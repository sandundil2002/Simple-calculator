import tkinter as tk
def display_window():
    root = tk.Tk()
    root.title("Calculator")
    width = 400
    height = 600
    display_width = root.winfo_screenwidth()
    display_height = root.winfo_screenheight()
    left = int(display_width/2 - width/2)
    top = int(display_height/2 - height/2)
    root.geometry(f'{width}x{height}+{left}+{top}')
    root.resizable(False, False)
    root.mainloop()

display_window()