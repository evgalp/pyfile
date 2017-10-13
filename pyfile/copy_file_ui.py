from tkinter import *
from tkinter import ttk

import logic
from logic import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.in_file_label = Label(root, text="Path to input file")
        self.in_file_label.grid(row=0, column=0, sticky=W)
        self.in_file_entry = Entry(root)
        self.in_file_entry.grid(row=0, column=1, sticky=E)

        self.out_file_label = Label(root, text="Path to output file")
        self.out_file_label.grid(row=1, column=0, sticky=W)
        self.out_file_entry = Entry(root)
        self.out_file_entry.grid(row=1, column=1, sticky=E)

        self.copy_btn = Button(root, text="Copy", command=self.client_copy_file)
        self.copy_btn.grid(row=2, column=0, sticky=W)
        self.exit_btn = Button(root, text="Exit", command=self.client_exit)
        self.exit_btn.grid(row=2, column=1, sticky=W)

        self.result_label = Label(root, text="none")
        self.result_label.grid(row=4, column=0, sticky=W)

    def get_entry_text(self, entry_name):
        return entry_name.get()

    def client_copy_file(self):
        in_path = self.get_entry_text(self.in_file_entry)
        out_path = self.get_entry_text(self.out_file_entry)
        if logic.copy_file(in_path, out_path):
            self.result_label.config(text="Copying done")
        else:
            self.result_label.config(text="Copying failed")



    def client_exit(self):
        exit()

if __name__ == '__main__':
    root = Tk()
    app = Window(root)
    root.mainloop()
