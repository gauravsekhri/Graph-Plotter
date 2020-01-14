from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from PIL import ImageTk, Image
from tkinter import messagebox
import json

LARGE_FONT= ("Verdana", 20)

class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Graph Plotter", font=LARGE_FONT)
        label.pack(pady=20,padx=20)

        button = tk.Button(self, text="Get Started",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        
#Creating First Page

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Choose any file", font=LARGE_FONT)
        label.grid(row=0, column=8, padx=0, pady=10)

        b4 = tk.Button(self, text="Select an Excel file",command=self.browsefunc)
        b4.grid(row=2, column=10, padx=0, pady=10)

        b5 = tk.Button(self, text="  Select a CSV file  ",command=self.browsef)
        b5.grid(row=5, column=2, padx=10, pady=10)

        b6 = tk.Button(self, text="  Select a JSON file  ",command=self.browsefg)
        b6.grid(row=8, column=2, padx=10, pady=10)

    #Function to browse files    
    
    def browsefunc(self):

        try:
            filename = filedialog.askopenfilename(filetype=
            (("Excel files", "*.xlsx"), ("all files", "*.*")))
            pathlabel.config(text=filename)
            df = pd.read_excel(filename)
            df.plot()
            plt.show()

        except:
            messagebox.showerror("Error", "No numeric data to plot")
        

    def browsef(self):

        try:
            filename = filedialog.askopenfilename(filetype=
            (("CSV files", "*.csv"), ("all files", "*.*")))
            pathlabel.config(text=filename)
            df = pd.read_csv(filename)
            df.plot()
            plt.show()

        except:
            messagebox.showerror("Error", "No numeric data to plot")

    def browsefg(self):

        try:
            filename = filedialog.askopenfilename(filetype=
            (("JSON files", "*.json"), ("all files", "*.*")))
            pathlabel.config(text=filename)

            with open(filename, 'rb') as f:
                data = f.readlines()
            data = map(lambda x: x.rstrip(), data)
            df = pd.read_json(data_json_str)

        except:
            messagebox.showerror("Error", "No numeric data to plot")

#Creating Second Page

class PageTwo(tk.Frame):

    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Select a type of graph", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

#Closing Message

def on_closing():
    if messagebox.askokcancel("Quit", "This Application was created by Gaurav Sekhri \n\n Hope you liked it !"):
        app.destroy()

        
app = SeaofBTCapp()

img = ImageTk.PhotoImage(Image.open("GP_icon.png"))
panel = Label(app, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")

app.protocol("WM_DELETE_WINDOW", on_closing)
pathlabel = Label(app)
pathlabel.pack()
app.wm_geometry("650x600")
app.title("Graph Plotter ")
app.iconbitmap('Icon.ico')
app.mainloop()
