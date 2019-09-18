from tkinter import Tk, Canvas

SIZE_MUL = 10

class GameGui:
	running = False

	def __init__(self, table):
		self.table = table

		self.master = Tk()
		self.master.title("Conway's Game of Life")

		self.canvas = Canvas(self.master, width=self.table.size*SIZE_MUL, height=self.table.size*SIZE_MUL)
		self.canvas.pack()

		self.canvas.bind(sequence="<Enter>", func=lambda event: self.canvas.focus_set())
		self.canvas.bind(sequence="<Button-1>", func=self.leftClick)
		self.canvas.bind(sequence="<B1-Motion>", func=self.leftClick)
		self.canvas.bind(sequence="<Key>", func=self.toggleRunning)
		
		self.updateCanvas()
		self.master.mainloop()


	def updateCanvas(self):
		if self.running:
			self.table.process()


		self.canvas.delete("all")
		for x in range(self.table.size):
			for y in range(self.table.size):
				if self.table.cells[x][y][0]:
						self.canvas.create_rectangle(x*SIZE_MUL, y*SIZE_MUL, (x+1)*SIZE_MUL, (y+1)*SIZE_MUL, fill='black', outline="white")


		self.canvas.after(100, self.updateCanvas)

	
	def flashCanvas(self):
		if self.running:
			self.table.process()


		self.canvas.delete("all")
		for x in range(self.table.size):
			for y in range(self.table.size):
				if self.table.cells[x][y][0]:
						self.canvas.create_rectangle(x*SIZE_MUL, y*SIZE_MUL, (x+1)*SIZE_MUL, (y+1)*SIZE_MUL, fill='black', outline="white")


	def leftClick(self, event):
		if not self.running:
			x, y = event.x, event.y
			cell_x = x // SIZE_MUL
			cell_y = y // SIZE_MUL

			self.table.cells[cell_x][cell_y][0] = 1

			self.flashCanvas()

		
	def toggleRunning(self, event):
		if event.char == ' ':
			if self.running:
				self.running = False
			else:
				self.running = True

			
			print("Running: {}".format(self.running))
