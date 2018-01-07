from tkinter import *
from tkinter import ttk

import logic
from logic import *

class Window(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.add_widgets()

    def add_widgets(self):

        self.in_path_label = Label(root, text="Path to input directory")
        self.in_path_label.grid(row=0,column=0)
        self.in_path_entry = Entry(root)
        self.in_path_entry.grid(row=0,column=1)

        self.in_ext_label = Label(root, text="Input files extension")
        self.in_ext_label.grid(row=1,column=0)
        self.in_ext_entry = Entry(root)
        self.in_ext_entry.grid(row=1,column=1)

        self.out_path_label = Label(root, text="Path to output directory")
        self.out_path_label.grid(row=2,column=0)
        self.out_path_entry = Entry(root)
        self.out_path_entry.grid(row=2,column=1)

        self.out_prefix_label = Label(root, text="Prefix for output files")
        self.out_prefix_label.grid(row=3,column=0)
        self.out_prefix_entry = Entry(root)
        self.out_prefix_entry.grid(row=3,column=1)

        self.out_ext_label = Label(root, text="Output files extension")
        self.out_ext_label.grid(row=4,column=0)
        self.out_ext_entry = Entry(root)
        self.out_ext_entry.grid(row=4,column=1)

        self.log_label = Label(root, text="logs here")
        self.log_label.grid(row=5)

        self.rename_btn = Button(root, text="Rename and copy", command=self.client_rename)
        self.rename_btn.grid(row=6,column=0)

        self.exit_btn = Button(root, text="Exit", command=self.client_exit)
        self.exit_btn.grid(row=6,column=1)


    def get_entry_text(self, entry_name):
        return entry_name.get()

    def client_rename(self):
        try:
            input_dir = self.get_entry_text(self.in_path_entry)
            input_ext = self.get_entry_text(self.in_ext_entry)

            output_dir = self.get_entry_text(self.out_path_entry)
            output_prefix = self.get_entry_text(self.out_prefix_entry)
            output_ext = self.get_entry_text(self.out_ext_entry)

            files_list = logic.get_files(input_dir, input_ext)
            logic.rename_files(files_list, output_prefix, output_ext, output_dir)

            self.log_label.config(text="Done")
        except Exception as e:
            self.log_label.config(text="Error")

    def client_exit(self):
        exit()

if __name__ == '__main__':
    root = Tk()
    app = Window(root)
    app.master.title("Rename and copy")
    root.mainloop()
