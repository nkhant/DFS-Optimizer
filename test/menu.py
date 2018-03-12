import tkinter as tk
from tkinter import *
import webbrowser

# File
def Save():
	print("Save")

def Load():
	print("Load")

def Options():
	print("Options")

# CSV
def Import():
	name = filedialog.askopenfilename()
	print(name)

def Export():
	print("Export File")

# Help
def GitHub():
	print("GitHub")
	webbrowser.open('https://github.com/gautam0826/DFS-Optimizer') # Links to Git Repo

def About():
	print("About")
	about = Toplevel()

	about.protocol("WM_DELETE_WINDOW", about.destroy)

	frame = Frame(about, width=500, height=300)
	frame.pack()
	frame.pack_propagate(False)
	
	var1 = StringVar()
	text1 = Label(frame, textvariable=var1)
	var1.set("Desktop application that reads an Excel file\n" +
	    "and lets users select what to maximize, minimize,\n" +
	    " and constraints to add.\n")
	text1.pack()

	text = Label(frame, text="Created by:", font='Helvetica 16 bold')
	text.pack()

	var2 = StringVar()
	text2 = Label(frame, textvariable=var2, font='Helvetica 12 bold', justify=LEFT)
	var2.set("Gautam Sarkar, Joseph Casteloes, Joelle Steichen,\n" +
	    "Ben Sherriff, Nagie Khant, Edmund Yu")
	text2.pack()
	
	about.mainloop()