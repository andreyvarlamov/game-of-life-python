from tkinter import *

class GameGui:
	def __init__(self, table):
		self.table = table

		self.master = Tk()
		self.master.title("Conway's Game of Life")

		self.canvas = Canvas(self.master, width=self.table.size*6, height=self.table.size*6)
		self.canvas.pack()

		# process cells and see which ones to display
		for index_y, row in enumerate(self.table.cells):
			for index_x, cell in enumerate(row):
				if cell.alive == 1:
					self.canvas.create_rectangle(index_x*5+1, index_y*5+1, index_x*5+6, index_y*5+6, fill='black')

		
		self.update_canvas()
		self.master.mainloop()

	def update_canvas(self):
		self.table.process()
		self.canvas.delete("all")
		for index_y, row in enumerate(self.table.cells):
			for index_x, cell in enumerate(row):
				if cell.alive == 1:
					self.canvas.create_rectangle(index_x*5, index_y*5, index_x*5+5, index_y*5+5, fill='black')

		self.canvas.after(10, self.update_canvas)

