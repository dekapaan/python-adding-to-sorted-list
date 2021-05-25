from tkinter import *
from tkinter import messagebox


class numToList:
    def __init__(self, master):
        # Adding window configuration
        self.master = master
        self.master.title('Adding numbers to a sorted list')
        self.master.config(bg='#575366')
        self.master.geometry('500x200')

        # Number entry label, delete button and add button
        self.enter_lbl = Label(self.master, text='Enter number:', font='monospace 11', bg='#575366', fg='white')
        self.enter_entry = Entry(self.master, font='monospace 10', bg='#D1E3DD')
        self.enter_btn = Button(self.master, text='Add', font='monospace 10', height=1, command=self.add_sort,
                                bg='#D1E3DD')
        self.delete_btn = Button(self.master, text='delete', font='monospace 10', height=1, command=self.delete,
                                 bg='#D1E3DD')
        self.enter_lbl.place(x=20, y=10)
        self.enter_entry.place(x=170, y=10)
        self.enter_btn.place(x=350, y=7)
        self.delete_btn.place(x=410, y=7)

        # Frame and label for displaying list
        self.list_frame = Frame(self.master, bg='#222', width=445, height=30)
        self.list_lbl = Label(self.list_frame, bg='#222', fg='white')
        self.list_frame.place(x=27, y=70)
        self.list_lbl.place(x=1, y=1)

        # Display list, clear, delete list, and exit buttons
        self.show_list_btn = Button(self.master, text='Display list', command=self.show_list, bg='#D1E3DD')
        self.clear_btn = Button(self.master, text='Clear', command=self.clear, bg='#D1E3DD')
        self.delete_list_btn = Button(self.master, text='Delete list', bg='#D1E3DD', command=self.delete_list)
        self.exit_btn = Button(self.master, text='Exit', command=exit, bg='#D1E3DD')
        self.show_list_btn.place(x=27, y=150)
        self.clear_btn.place(x=137, y=150)
        self.exit_btn.place(x=420, y=150)
        self.delete_list_btn.place(x=315, y=150)

        # Number list
        self.num_list = list()

    # Function to clear fields
    def clear(self):
        self.enter_entry.delete(0, END)
        self.list_lbl.config(text='')

    # Function to delete text in fields
    def delete(self):
        try:
            self.num_list.remove(int(self.enter_entry.get()))
            self.enter_entry.delete(0, END)
        except ValueError:
            text = '{} not in the list'.format(self.enter_entry.get())
            messagebox.showerror(message=text)

    # Function to add numbers to sorted list
    def add_sort(self):
        try:
            # Add number to list
            number = int(self.enter_entry.get())
            self.num_list.append(number)
            self.enter_entry.delete(0, END)

            # Sorts list when new entries are given
            if len(self.num_list) >= 2:
                for i in range(len(self.num_list)):
                    for j in range(len(self.num_list) - 1):
                        if self.num_list[j] > self.num_list[j + 1]:
                            self.num_list[j], self.num_list[j + 1] = self.num_list[j + 1], self.num_list[j]

        # ValueError if integer is not inputted
        except ValueError:
            messagebox.showerror(message='Only integer allowed as entry')

    # Function to display list
    def show_list(self):
        self.list_lbl.config(text=self.num_list)

    # Function to delete list items
    def delete_list(self):
        self.num_list = []


root = Tk()
numToList(root)
root.mainloop()
