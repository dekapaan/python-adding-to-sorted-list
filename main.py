from tkinter import *
from tkinter import messagebox


class numToList:
    def __init__(self, master):
        # changing window configurations
        self.master = master
        self.master.title('Adding numbers to a sorted list')
        self.master.config(bg='#575366')
        self.master.geometry('490x150')

        # User entry label and entry field
        self.enter_lbl = Label(self.master, text='Enter number:', font='monospace 11', bg='#575366', fg='white')
        self.enter_entry = Entry(self.master, font='monospace 10', bg='#D1E3DD')
        self.enter_btn = Button(self.master, text='Add to list', font='monospace 10', height=1, command=self.add_sort,
                                bg='#D1E3DD')
        self.enter_lbl.place(x=20, y=10)
        self.enter_entry.place(x=170, y=10)
        self.enter_btn.place(x=350, y=7)

        # Frame and label to display list
        self.list_frame = Frame(self.master, bg='#222', width=445, height=30)
        self.list_lbl = Label(self.list_frame, bg='#222', fg='white')
        self.list_frame.place(x=20, y=70)
        self.list_lbl.place(x=1, y=1)

        # Buttons
        self.show_list_btn = Button(self.master, text='Display list', command=self.show_list, bg='#D1E3DD')
        self.clear_btn = Button(self.master, text='Clear', command=self.clear, bg='#D1E3DD')
        self.exit_btn = Button(self.master, text='Exit', command=exit, bg='#D1E3DD')
        self.show_list_btn.place(x=20, y=110)
        self.clear_btn.place(x=130, y=110)
        self.exit_btn.place(x=413, y=110)

        self.num_list = list()

    # function to clear fields
    def clear(self):
        self.enter_entry.delete(0, END)
        self.list_lbl.config(text='')

    # funtion to add new number to list and bubble-sort the list
    def add_sort(self):
        try:
            number = int(self.enter_entry.get())
            self.num_list.append(number)
            self.enter_entry.delete(0, END)

            if len(self.num_list) >= 2:
                for i in range(len(self.num_list)):
                    for j in range(len(self.num_list) - 1):
                        if self.num_list[j] > self.num_list[j + 1]:
                            self.num_list[j], self.num_list[j + 1] = self.num_list[j + 1], self.num_list[j]

        # ValueError if integer not entered
        except ValueError:
            messagebox.showerror(message='Only integer allowed as entry')

    # Function to display list
    def show_list(self):
        self.list_lbl.config(text=self.num_list)


root = Tk()
numToList(root)
root.mainloop()
