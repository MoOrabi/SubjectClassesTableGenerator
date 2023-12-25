from tkinter import *
import tkinter as tk
from  tkinter import ttk
import tkinter.font as font

class RoundedButton(tk.Canvas):
    t=''
    def __init__(self, parent, border_radius, padding, color, text='', command=None):
        tk.Canvas.__init__(self, parent, borderwidth=0,
                           relief="raised", highlightthickness=0, bg='#ffffff'  )
        self.command = command
        self.clipboard_append(text)
        self.t = text
        font_size = 12
        self.font = font.Font(size=font_size, family='Helvetica')
        self.id = None
        height = font_size + (1 * padding)
        width = self.font.measure(text)+(1*padding)
        width = width if width >= 80 else 80
        if border_radius > 0.5*width:
            print("Error: border_radius is greater than width.")
            return None
        if border_radius > 0.5*height:
            print("Error: border_radius is greater than height.")
            return None
        rad = 2*border_radius
        def shape():
            self.create_arc((0, rad, rad, 0),start=90, extent=90, fill=color, outline=color)
            self.create_arc((width-rad, 0, width, rad), start=0, extent=90, fill=color, outline=color)
            self.create_arc((width, height-rad, width-rad,height), start=270, extent=90, fill=color, outline=color)
            self.create_arc((0, height-rad, rad, height), start=180, extent=90, fill=color, outline=color)
            return self.create_polygon((0, height-border_radius, 0, border_radius, border_radius, 0, width-border_radius, 0, width,border_radius, width, height-border_radius, width-border_radius, height, border_radius, height),fill=color, outline=color)
        id = shape()
        (x0, y0, x1, y1) = self.bbox("all")
        width = (x1-x0)
        height = (y1-y0)
        self.configure(width=width, height=height)
        self.create_text(width/2 - 2, height/2 - 2, text=text, fill='#ffffff', font=self.font)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        
        
    def _on_press(self, event):
        self.itemconfig("all", fill='#d2d6d3')
        # self.create_text(self.winfo_width() / 2, self.winfo_height() / 2, text=self.t, fill='#ffffff', font=self.font)

    def _on_release(self, event):
        self.itemconfig("all", fill="#172f5f")
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2, text=self.t, fill='#ffffff', font=self.font)
        if self.command is not None:
            self.command()

    def disable(self):
        # self.unbind("<1>")
        # This method will disable the button by unbinding the events and changing the color to gray
        self.unbind("<ButtonPress-1>")
        self.unbind("<ButtonRelease-1>")
        self.itemconfig("all", fill="#a9a9a9")
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2, text=self.t,
                         fill='#ffffff', font=self.font)

    def first_disable(self):
        # self.unbind("<1>")
        # This method will disable the button by unbinding the events and changing the color to gray
        self.unbind("<ButtonPress-1>")
        self.unbind("<ButtonRelease-1>")
        self.itemconfig("all", fill="#a9a9a9")
        self.create_text(self.winfo_width() + 42, self.winfo_height() + 12, text=self.t,
                         fill='#ffffff', font=self.font)
    
    def enable(self):
        # self.config(state="normal")
        # This method will enable the button by binding the events and changing the color to the original one
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        self.itemconfig("all", fill="#172f5f")
        # self.create_text(self.winfo_width()+42, self.winfo_height()+12, text=self.t, fill='#ffffff', font=self.font)
        self.create_text(self.winfo_width() / 2, self.winfo_height() / 2, text=self.t, fill='#ffffff', font=self.font)


##################################################################
##################################################################

class tkinterTable(tk.Frame):
    rh=0
    def __init__(self, parent,  height, width, columns, rowheigh ,style):
        tk.Frame.__init__(self, parent)
        self.headers = []
        self.rows = 0
        
        self.rh=rowheigh
        
        self.game_frame = tk.Frame(self)
        self.game_frame.pack()
        
        self.my_game = ttk.Treeview(self.game_frame, height=height, style=style+'.Treeview')
        
        style1 = ttk.Style()
        style1.configure(style+'.Treeview', rowheight=self.rh) # Set the row height
        style1.configure(style+'.Treeview.Heading', font=('Arial', 20, 'bold')) # Set the font of the headings
        style1.configure('Treeview', font=('Arial', 14))

        
        self.my_game['columns'] = [str(i) for i in range(1, columns + 1)]

        self.my_game.column("#0", width=0,  stretch=tk.NO)
        for i in range(1,columns + 1):
            self.my_game.column(str(i),anchor=tk.CENTER,width=width)
            
        self.my_game.heading("#0",text="",anchor=tk.CENTER)
        for i in range(1,columns + 1):
            self.my_game.heading(str(i),text=str(i),anchor=tk.CENTER)
        '''     
        # Add a scrollbar to the treeview
        self.scrollbar = ttk.Scrollbar(self.game_frame, orient="vertical", command=self.my_game.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.my_game.configure(yscrollcommand=self.scrollbar.set)
        '''
        
        self.my_game.pack()

        
        print(self.rh)
    def insert_row(self, data):
        self.my_game.insert(parent='',index='end',iid=self.rows,text='',values=data)
        self.rows=self.rows+1

    def edit_item(self, row, column, value):
        self.my_game.set(item=row, column=column, value=value)
        

##################################################################
##################################################################
class LabelTable():
    # Initialize a constructor
    def __init__(self, gui,list=[]):
        l=[' ','Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday']
        d=['09:00-10:30','10:30-12:00','12:00-01:30','01:30-03:00','03:00-04:30']
       
        # Create a canvas widget to display the table
        self.canvas = Canvas(gui, width=1300, height=700)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Create a scrollbar widget and attach it to the canvas
        self.scrollbar = Scrollbar(gui, orient=VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Create a frame widget to hold the labels
        self.frame = Frame(self.canvas, bg='white')
        self.canvas.create_window((0, 0), window=self.frame, anchor=NW)

        # An approach for creating the table
        row0 = 0
        for i in range(0, 25, +4):
            if i == 0:
                self.label = Label(
                            self.frame, # Change the parent widget to the frame
                            text=l[row0],
                            width=9, height=2,
                            fg="Black",
                            font=("Arial", 20, "bold"),
                            bg="white"
                        )
            else :
                self.label = Label(
                                self.frame, # Change the parent widget to the frame
                                text=l[row0],
                                width=9, height=8,
                                fg="#333333",
                                font=("Arial", 20, "bold"),
                                bg="#3498db"
                            )
            self.label['borderwidth'] = 1
            self.label['relief'] = GROOVE
            self.label.grid(row=i, column=0, rowspan=4)
            row0 = row0+1
            
        col0 = 0
        for i in range(1, 6):
            
            self.label = Label(
                            self.frame, # Change the parent widget to the frame
                            text=d[col0],
                            width=13, height=2,
                            fg="#333333",
                            font=("Arial", 20, "bold"),
                            bg="#3498db"
                        )
            self.label['borderwidth'] = 1
            self.label['relief'] = GROOVE
            self.label.grid(row=0, column=i)
            col0 = col0+1
        
        self.labels = []
        row1 = 0
        for i in range(4, 28):
            col = 0
            self.labels.append([])
            for o in range(1, 6):
                self.label = Label(
                            self.frame, # Change the parent widget to the frame
                            text=list[row1][col],
                            width=29, height=3,
                            font=("Arial", 8, "bold"),
                            bg="#f5f5f5",
                            fg="#222222"
                        )
                self.label['borderwidth'] = 1
                self.label['relief'] = GROOVE
                self.label.grid(row=i, column=o)
                self.labels[-1].append(self.label)
                col = col+1
            row1 = row1+1

        # Update the canvas scrollregion to fit the frame
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        
    # Define a method to edit an item in the table
    def edit_item(self, row, column, value):
        # Check if the row and column are valid
        if 0 <= row < len(self.labels) and 0 <= column < len(self.labels[0]):
            # Use the set method of the label to change the text
            self.labels[row][column].config(text=value)
        else:
            # Print an error message if the row or column are out of range
            print("Invalid row or column")



