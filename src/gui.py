from tkinter import *
import tkinter as tk
# Table class


from tkinter import *  # Import the tkinter module


class Table():
    # Initialize a constructor
    def __init__(self, gui):
        l = [' ', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
        d = ['09:00 - 10:30', '10:30 - 12:00', '12:00 - 01:30', '01:30 - 03:00', '03:00 - 04:30']
        list = [
            ("ID", "Name", "City", "Age"),
            ("Vanessa", "Gorge", "California", "California"),
            ("Karachi", "Maria", "New York", "Maria"),
            ("Ali", "Albert", "Berlin", "Name"),
            ("Boston", "Harry", "Chicago", "Ali"),
            ("ID", "Name", "City", "Age"),
            ("Vanessa", "Gorge", "California", "California"),
            ("Karachi", "Maria", "New York", "Maria"),
            ("Ali", "Albert", "Berlin", "Name"),
            ("Boston", "Harry", "Chicago", "Ali"),
            ("ID", "Name", "City", "Age"),
            ("Vanessa", "Gorge", "California", "California"),
            ("Karachi", "Maria", "New York", "Maria"),
            ("Ali", "Albert", "Berlin", "Name"),
            ("Boston", "Harry", "Chicago", "Ali"),
            ("ID", "Name", "City", "Age"),
            ("Vanessa", "Gorge", "California", "California"),
            ("Karachi", "Maria", "New York", "Maria"),
            ("Ali", "Albert", "Berlin", "Name"),
            ("Boston", "Harry", "Chicago", "Ali"),
            ("ID", "Name", "City", "Age"),
            ("Vanessa", "Gorge", "California", "California"),
            ("Karachi", "Maria", "New York", "Maria"),
            ("Ali", "Albert", "Berlin", "Name"),
            ("Boston", "Harry", "Chicago", "Ali"),
            ("ID", "Name", "City", "Age"),
            ("Vanessa", "Gorge", "California", "California"),
            ("Karachi", "Maria", "New York", "Maria"),
            ("Ali", "Albert", "Berlin", "Name"),
            ("Boston", "Harry", "Chicago", "Ali"),
            ("ID", "Name", "City", "Age"),
            ("Vanessa", "Gorge", "California", "California"),
            ("Karachi", "Maria", "New York", "Maria"),
            ("Ali", "Albert", "Berlin", "Name"),
            ("Boston", "Harry", "Chicago", "Ali")
        ]
        # Create a canvas widget to display the table
        self.canvas = Canvas(gui, width=1050, height=600)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a scrollbar widget and attach it to the canvas
        self.scrollbar = Scrollbar(gui, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame widget to hold the labels
        self.frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor=NW)

        # An approach for creating the table
        row0 = 0
        for i in range(0, 31, +5):
            if i == 0:
                self.label = Label(
                    self.frame,  # Change the parent widget to the frame
                    text=l[row0],
                    width=10, height=2,
                    fg="Black",
                    font=("Arial", 20, "bold")
                )
            else:
                self.label = Label(
                    self.frame,  # Change the parent widget to the frame
                    text=l[row0],
                    width=10, height=8,
                    fg="Black",
                    font=("Arial", 20, "bold")
                )
            self.label['borderwidth'] = 1
            self.label['relief'] = GROOVE
            self.label.grid(row=i, column=0, rowspan=5)
            row0 = row0 + 1

        col0 = 0
        for i in range(1, 6):
            self.label = Label(
                self.frame,  # Change the parent widget to the frame
                text=d[col0],
                width=10, height=2,
                fg="Black",
                font=("Arial", 20, "bold")
            )
            self.label['borderwidth'] = 1
            self.label['relief'] = GROOVE
            self.label.grid(row=0, column=i)
            col0 = col0 + 1

        row1 = 0
        for i in range(5, 35):
            col = 0
            for o in range(1, 5):
                self.label = Label(
                    self.frame,  # Change the parent widget to the frame
                    text=list[row1][col],
                    width=10, height=1,
                    fg="Black",
                    font=("Arial", 15, "bold")
                )
                self.label['borderwidth'] = 1
                self.label['relief'] = GROOVE
                self.label.grid(row=i, column=o)
                col = col + 1
            row1 = row1 + 1

        # Update the canvas scrollregion to fit the frame
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


root = tk.Tk()
root.title('PythonGuides')
root.wm_minsize(1366, 768)
root.wm_maxsize(1366, 768)
root['bg'] = '#ffffff'
window = tk.Label(root, width=str(1366), height=str(768))
window.place(x=0, y=0)

# create root window

table = Table(window)

root.mainloop()
