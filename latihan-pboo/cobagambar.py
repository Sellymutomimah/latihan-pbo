import tkinter as tk

jendela= tk.Tk()
jendela.title("Gambar Label - selly")

logo = tk.PhotoImage(file="spongebob.png") 
logo_label = tk.Label(image=logo)
logo_label.pack()
tk.mainloop()