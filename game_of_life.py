import gol_display
import random

# class for a cell
class Cell:
	pos_x = 0
	pos_y = 0
	alive = 1

	def __init__(self, pos_x , pos_y, alive):
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.alive = alive

	def die(self):
		self.alive = 0

	def live(self):
		self.alive = 1

class Table:
	cells = []

	def __init__(self, size_x, size_y):
		self.generateCells(size_x, size_y)


	def generateCells(self, size_x, size_y):
		for i in range(0, table_size_x):
			cell_row = []
			for j in range(0, table_size_y):
				cell_row.append(Cell(i, j, random.randint(0,1)))\

			self.cells.append(cell_row)


	def neighbors(self, cell):
		neighbors = []
		try:
			neighbors.append(self.cells[cell.pos_x][cell.pos_y+1])
		except IndexError:
			None

		try:	
			neighbors.append(self.cells[cell.pos_x+1][cell.pos_y+1])
		except IndexError:
			None

		try:
			neighbors.append(self.cells[cell.pos_x+1][cell.pos_y])
		except IndexError:
			None

		try:	
			neighbors.append(self.cells[cell.pos_x+1][cell.pos_y-1])
		except IndexError:
			None
	
		try:
			neighbors.append(self.cells[cell.pos_x][cell.pos_y-1])
		except IndexError:
			None
	
		try:
			neighbors.append(self.cells[cell.pos_x-1][cell.pos_y-1])
		except IndexError:
			None

		try:
			neighbors.append(self.cells[cell.pos_x-1][cell.pos_y])
		except IndexError:
			None
	
		try:
			neighbors.append(self.cells[cell.pos_x-1][cell.pos_y+1])
		except IndexError:
			None

		return neighbors

	def processCell(self, cell):
		neighbors = self.neighbors(cell)
		print(str(len(neighbors))+": ", end="")
		result = 0
		neighbors_alive = 0 
		#underpopulation, normal, overpopulation, reproduction
		for neighbor in neighbors:
			if neighbor.alive == 1:
				neighbors_alive += 1

		print(str(neighbors_alive) + ", " + str(result))		

		if cell.alive == 1:
			if neighbors_alive < 2:
				cell.die()
			elif neighbors_alive > 3:
				cell.die()
			else:
				None
		else:
			if neighbors_alive == 3:
				cell.live()
			else: 
				None


		return result


	def process(self):
		for row in self.cells:
			for cell in row:
				self.processCell(cell)



table_size_x = 3
table_size_y = 3

table = Table(table_size_x, table_size_y)

gol_display.printTable(table)
input("Press Enter to continue...")
table.process()
gol_display.printTable(table)







