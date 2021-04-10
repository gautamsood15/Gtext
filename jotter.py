# Importing Tkinter

import tkinter
import os 
from tkinter import *

from tkinter.messagebox import *	# used to create the whitebox called notepad

from tkinter.filedialog import *    # used to save or open files 



# --------------------- Adding Menu ------------------------------------------------------------------------------

self.__thisTextArea.grid(sticky = N + E + S + W)       # adding controls(widget)

self.__thisFileMenu.add_command(label = "New", command = self.__newFile)                # adding label to opening new file function

self.__thisFileMenu.add_command(label = "Open", command = self.__openFile)              # adding label to opening a file function

self.__thisFileMenu.add_command(label = "Save", command = self.__saveFile)              # adding label to save current file function

self.__thisFileMenu.add_separator()                                                     # to create a line in the dialog

self.__thisFileMenu.add_command(label = "Exit", command = self.__quitApplication)       # adding label to exit function 

self.__thisFileMenu.add_cascade(label = "File", menu = self.__thisFileMenu)             # ADDING all the above functions to File Tab







self.__thisEditMenu.add_command(label = "Cut", command = self.__cut)                    # adding label to cut function 

self.__thisEditMenu.add_command(label = "Copy", command = self.__copy)                  # adding label to copy function

self.__thisEditMenu.add_command(label = "Paste", command = self.__paste)                # adding label to paste function

self.__thisMenuBar.add_cascade(label = "Edit", menu = self.__thisEditMenu)              # ADDING all the above functions to Edit Tab








self.__thisHelpMenu.add_command(label = "About Jotter", command = self.__showAbout)     # adding label to description function


self.__thisMenuBar.add_cascade(label = "Help", menu = self.__thisHelpMenu)              # adding lable to help function
  
self.__root.config(menu = self.__thisMenuBar)                                           # ADDING all the above function to                                          
  
self.__thisScrollBar.pack(side = RIGHT, fill = Y)



# Scrollbar will adjust automatically
# according to the content
self.__thisScrollBar.config(command = self.__thisTextArea.yview)
self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set)





