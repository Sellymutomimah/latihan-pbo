import tkinter as tk

window =  tk.Tk()
window.title("entry -  selly")

def show(): 
    tk.Label(text=e1.get()).grid(row=3,column=0) 
    tk.Label(text=e2.get()).grid(row=3,column=1)

tk.Label(window, text="First Name").grid(row=0) 
tk.Label(window, text="Last Name").grid(row=1)

e1 = tk.Entry(window) 
e2 = tk.Entry(window) 
b1 = tk.Button(text="show", command=show)

e1.grid(row=0, column=1) 
e2.grid(row=1, column=1) 
b1.grid(row=2, column=1)

window.mainloop()