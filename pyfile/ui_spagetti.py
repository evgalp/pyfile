from tkinter import *
from tkinter import ttk

root = Tk()

in_file_label = Label(root, text="Path to input file").grid(row=0, column=0, sticky=W)
in_file_entry = Entry(root).grid(row=0, column=1, sticky=E)

out_file_label = Label(root, text="Path to output file").grid(row=1, column=0, sticky=W)
out_file_entry = Entry(root).grid(row=1, column=1, sticky=E)

copy_btn = Button(root, text="Copy").grid(row=2, column=0, sticky=W)
exit_btn = Button(root, text="Exit").grid(row=2, column=1, sticky=E)

def client_exit():
    exit()


root.mainloop()
