import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import settings
from menu import *

# Starting variables for fixed settings
lineups, players, maxCost = 0, 0, 0

#=============
#    Menu
#=============
menu = Menu(settings.app.root)
settings.app.root.config(menu=menu)

#=============
#    FILE
#=============
filemenu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Save Settings", command=Save)
filemenu.add_command(label="Load Settings", command=Load)
filemenu.add_command(label="Options", command=Options)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=settings.app.root.destroy)

#=============
#    CSV
#=============
csvmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="CSV", menu=csvmenu)
csvmenu.add_command(label="Import", command=Import)
csvmenu.add_command(label="Export", command=Export)

#=============
#    HELP
#=============
helpmenu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="GitHub", command=GitHub)
helpmenu.add_command(label="About", command=About)

frame = Frame(settings.app.root, width=settings.app.w, height=settings.app.h, background='red')
frame.pack(fill=BOTH)
frame.pack_propagate(False) # Stop frame from resizing to widgets

#=============
# Top Frame
#=============
top = Frame(frame, width=settings.app.w, height=settings.app.h/2.2, background='white')
top.grid(row=0)
top.grid_propagate(False) # Stop frame from resizing to widgets
for i in range(0,17):
	top.grid_rowconfigure(i, weight=1)
for j in range(0,49):
	top.grid_columnconfigure(j, weight=1)

# Top Widgets
saveSetting = Button(top, text='Save Settings', command=Save)
saveSetting.grid(row=0, column=19)
loadSetting = Button(top, text='Load Settings', command=Load)
loadSetting.grid(row=0, column=20)
addSetting = Button(top, text='Add Setting', command=Add)
addSetting.grid(row=0, column=21)

importBtn = Button(top, text='Import CSV', command=Import)
importBtn.grid(row=16, column=0)
exportBtn = Button(top, text='Export CSV', command=Export)
exportBtn.grid(row=16, column=1)

optimizeBtn = Button(top, text='Optimize', height=2, width=20, command=Optimize)
optimizeBtn.grid(row=15, rowspan=2, column=19, columnspan=3)

text1 = 'Number of Lineups: ' + repr(lineups)
setting1 = Label(top, text=text1)
setting1.grid(row=1, columnspan=10, sticky=W)

text2 = 'Number of Players: ' + repr(players)
setting2 = Label(top, text=text2)
setting2.grid(row=2, columnspan=10, sticky=W)

text3 = 'Max Cost: ' + repr(maxCost)
setting3 = Label(top, text=text3)
setting3.grid(row=3, columnspan=10, sticky=W)

#=============
# Split Frame
#=============
split = Frame(frame, width=settings.app.w, height=1, background='black')
split.grid(row=18)

#=============
# Bot Frame
#=============
bot = Frame(frame, width=settings.app.w, height=settings.app.h/2, background='white')
bot.grid(row=19)
bot.grid_propagate(False) # Stop frame from resizing to widgets
for i in range(19,36):
	bot.grid_rowconfigure(i, weight=1)

settings.app.root.mainloop()