from tkinter import *

SIZE_MUL = 10

class GameGui:
	

	def __init__(self, table):
		self.table = table

		self.master = Tk()
		self.master.title("Conway's Game of Life")

		self.canvas = Canvas(self.master, width=self.table.size*SIZE_MUL, height=self.table.size*SIZE_MUL)
		self.canvas.pack()

		# process cells and see which ones to display
		for index_y, row in enumerate(self.table.cells):
			for index_x, cell in enumerate(row):
				if cell.alive == 1:
					self.canvas.create_rectangle(index_x*SIZE_MUL, index_y*SIZE_MUL, (index_x+1)*SIZE_MUL, (index_y+1)*SIZE_MUL, fill='black', outline="white")

		
		self.update_canvas()
		self.master.mainloop()

	def update_canvas(self):
		self.table.process()
		self.canvas.delete("all")
		for index_y, row in enumerate(self.table.cells):
			for index_x, cell in enumerate(row):
				if cell.alive == 1:
					self.canvas.create_rectangle(index_x*SIZE_MUL, index_y*SIZE_MUL, (index_x+1)*SIZE_MUL, (index_y+1)*SIZE_MUL, fill='black', outline="white")

		self.canvas.after(50, self.update_canvas)

