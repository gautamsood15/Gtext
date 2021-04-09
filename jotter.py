# Importing Tkinter

import tkinter
import os 
from tkinter import *

from tkinter.messagebox import *	# used to create the whitebox called notepad

from tkinter.filedialog import *    # used to save or open files 



# ---------------------------------------- ADDING MENU -----------------------------------------------------------




self.__thisTextArea.grid(sticky = N + E + S + W)       # adding controls(widget)

self.__thisFileMenu.add_command(label = "New", command = self.__newFile)                # adding label to opening new file function

self.__thisFileMenu.add_command(label = "Open", command = self.__openFile)              # adding label to opening a file function

self.__thisFileMenu.add_command(label = "Save", command = self.__saveFile)              # adding label to save current file function

self.__thisFileMenu.add_separator()                                                     # Adds a separator line to the menu

self.__thisFileMenu.add_command(label = "Exit", command = self.__quitApplication)       # adding label to exit function 

self.__thisFileMenu.add_cascade(label = "File", menu = self.__thisFileMenu)             # ADDING all the above functions to File Tab







self.__thisEditMenu.add_command(label = "Cut", command = self.__cut)                    # adding label to cut function 

self.__thisEditMenu.add_command(label = "Copy", command = self.__copy)                  # adding label to copy function

self.__thisEditMenu.add_command(label = "Paste", command = self.__paste)                # adding label to paste function

self.__thisMenuBar.add_cascade(label = "Edit", menu = self.__thisEditMenu)              # ADDING all the above functions to Edit Tab








self.__thisHelpMenu.add_command(label = "About Jotter", command = self.__showAbout)     # adding label to description function

self.__thisMenuBar.add_cascade(label = "Help", menu = self.__thisHelpMenu)              # ADDING all the above function to  
  



self.__root.config(menu = self.__thisMenuBar)                                           # adding menu bar to whitebox                                        
  




self.__thisScrollBar.pack(side = RIGHT, fill = Y)                        # adding scrollbar to the right of whitebox on y axis                               

self.__thisScrollBar.config(command = self.__thisTextArea.yview)      # Scrollbar will adjust automatically according to the content 
self.__thisTextArea.config(yscrollcommand = self.__thisScrollBar.set)    










#----------------------------------------- ADDING THE FUNCTIONALITY ------------------------------------------------



def __quitApplication(self):                # function for exit button
	self.__root.destroy()

def __showAbout(self):                      # function for About Jotter button
	showinfo("Jotter", "Jotter is a simple text editor written in Python. It is a basic text-editing program which enables computer users to create documents.")

def __openFile(self):						# function for Open button

	self.__file = askopenfilename(defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents", "*.txt"), ("Python","*.py")])     

	if self.__file == "":                   # if file is not named, add None to __file variable
		self.__file = None

	else:
		self.__root.title(os.path.basename(self.__file) + " - Jotter")         # adding filename to titlebar
		self.__thisTextArea.delete(1.0,END)                                    # clearing the whitebox

		file = open(self.__file, "r")                                      # open selected file add data to whitebox and close file
		self.__thisTextArea.insert(1.0, file.read())
		file.close()


def __newFile(self):                              # function for new button
	self.__root.title("New File - Jotter")
	self.__file = None
	self.__thisTextArea.delete(1.0, END)


def __saveFile(self):                            # function for save button

	if self.__file == None:  
		self.__file = asksaveasfilename(initialfile='', defaultextension=".txt", filetypes=[("All Files","*.*"), ("Text Documents","*.txt"), ("Python","*.py")])


		if self.__file == "":
			self.__file = None

		else:
			file = open(self.__file, "w")
			file.write(self.__thisTextArea.get(1.0, END))
			file.close()

			self.__root.title(os.path.basename(self.__file) + " - Jotter")

	else:
		file = open(self.__file "w")
		file.write(self.__thisTextArea.get(1.0, END))
		file.close()


def __cut(self):                                         # function for Cut button
	self.__thisTextArea.event_generate("<<Cut>>")

def __copy(self):                                        # function for copy button
	self.__thisTextArea.event_generate("<<Copy>>")

def __paste(self):                                       # function for paste button
	self.__thisTextArea.event_generate("<<Paste>>")
