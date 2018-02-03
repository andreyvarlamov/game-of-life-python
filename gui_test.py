from tkinter import *

class GuiEx1:
	def __init__(self, master):
		self.master = master
		master.title('A Simple GUI')

		# create a label object in the root
		self.label = Label(master, text='This is my first GUI')
		# add the label object to the root
		self.label.pack()

		# create a button, command - takes in a function name to execute
		self.greet_button = Button(master, text='Greet', command=self.greet)
		self.greet_button.pack()

		# create abutton root.quit - Tk function to quit
		self.close_button = Button(master, text='Close', command=master.quit)
		self.close_button.pack()

	def greet():
		print('Greetings!')

class GuiEx2:

	LABEL_TEXT = ["This is our first GUI!",
       				"Actually, this is our second GUI.",
       				"We made it more interesting...",
        			"...by making this label interactive.",
        			"Go on, click on it again."]

	def __init__(self, master):
		self.master = master
		master.title("A simple GUI")

		self.label_index = 0
		self.label_text = StringVar()
		self.label_text.set(self.LABEL_TEXT[self.label_index])
		self.label = Label(master, textvariable=self.label_text)
		self.label.bind("<Button-1>", self.cycle_label_text)
		self.label.pack()

		self.greet_button = Button(master, text='Greet', command=self.greet)
		self.greet_button.pack()

		self.close_button = Button(master, text='Close', command=master.quit)
		self.close_button.pack()

	def greet(self):
		print('Greetings!')

	def cycle_label_text(self, event):
		self.label_index += 1
		self.label_index %= len(self.LABEL_TEXT)
		self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
guiEx2 = GuiEx2(root)
# starts looping to accept events from the window
root.mainloop()


""" Other tkinter widgets:
	Frame - container widget; its own border and background
	Toplevel - container widget; seprate window
	Canvas - for drawing graphics
	Text
	Button
	Message - same as text, but for longer bodies of text(wrapped)
	Scrollbar
	Checkbutton, Radiobutton, Listbox, Entry, Scale
	Menu and Menubutton"""

""" Three geometry managers in tkinter:
	pack() - arranges widgets vertically inside their parent container, from top down
		pack(side= ) - optional - BOTTOM, LEFT, RIGHT, TOP
	grid() - position widgets using a grid layout
		parameters: row=1, column=1, columnspan, rowspan=2, sticky=(stick to a particular side) - N, S, E, W, NE, W+E(stretched horizontally)
	!!!! don't use pack and grid inside same window	
	place() - explicit position and size (pixels) - not recommended"""

""" Custom events.
	bind() method - in every widget class"""
