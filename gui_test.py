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

class GuiEx3Calculator:
	def __init__(self, master):
		self.master = master
		master.title("Calculator")

		self.total = 0
		self.entered_number = 0

		self.total_label_text = IntVar()
		self.total_label_text.set(self.total)
		self.total_label = Label(master, textvariable=self.total_label_text)

		self.label = Label(master, text="Total:")

		# wrap the command with Tk register
		vcmd = master.register(self.validate)
		# validate - validates the contents (with the validatecommand method): focusin, focusout, key - events
		# validatecommand - pass a tuple - %P
		self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

		# wrap update functions in lambda funtions (to spcify which parameters to pass)
		self.add_button = Button(master, text="+", command=lambda: self.update("add"))
		self.subtract_button = Button(master, text='-', command=lambda: self.update("subtract"))
		self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

		# LAYOUT
		self.label.grid(row=0, column=0, sticky=W)
		self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

		self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

		self.add_button.grid(row=2, column=0)
		self.subtract_button.grid(row=2, column=1)
		self.reset_button.grid(row=2, column=2, sticky=W+E)

	def validate(self, new_text):
		if not new_text:
			self.entered_number = 0
			return True

		try:
			self.entered_number = int(new_text)
			return True
		except ValueError:
			return False

	def update(self, method):
		if method == "add":
			self.total += self.entered_number
		elif method == "subtract":
			self.total -= self.entered_number
		else:
			self.total = 0

		self.total_label_text.set(self.total)
		# clear the entry widget from first index (0) to END; also deletion triggers validation - updates entered_number to 0
		self.entry.delete(0, END)


root = Tk()
guiEx3Calculator = GuiEx3Calculator(root)
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
	bind() method - in every widget class
	events - <Button-1> - LMK, <Button-2> - MMK, <Button-3> - RMK
	<ButtonRelease-1> <B1-Motion>
	<Enter> and <Leave> - mouse cursor entered or left widget
	<Key> - keyboard key, also specific key, e.g. <Return> <Shift-Up>
	<Configure> - widget changed size"""

""" StringVar, IntVar, etc. - tkinter variable wrapper - e.g. for dynamic text etc."""

""" 
