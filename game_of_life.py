import gol_display

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

class Table:
	cells = []

	def __init__(self, size_x, size_y):
		self.generateCells(size_x, size_y)


	def generateCells(self, size_x, size_y):
		for i in range(0, table_size_x):
			cell_row = []
			for j in range(0, table_size_y):
				cell_row.append(Cell(i, j, 0))\

			self.cells.append(cell_row)


	def neighbors(self, cell):
		neighbors = []

		neighbors.append(cells[cell.pos_x][cell.pos_y+1])
		neighbors.append(cells[cell.pos_x+1][cell.pos_y+1])
		neighbors.append(cells[cell.pos_x+1][cell.pos_y])
		neighbors.append(cells[cell.pos_x+1][cell.pos_y-1])
		neighbors.append(cells[cell.pos_x][cell.pos_y-1])
		neighbors.append(cells[cell.pos_x-1][cell.pos_y-1])
		neighbors.append(cells[cell.pos_x-1][cell.pos_y])
		neighbors.append(cells[cell.pos_x-1][cell.pos_y+1])

		return neighbors

	def checkCell(self, cell):
		neighbors = self.neighbors(cell)
		result = 0
		#underpopulation, normal, overpopulation, reproduction
		for neighbor in neighbors

	def process(self):
		for row in self.cells:
			for cell in row:



table_size_x = 10
table_size_y = 10

table = Table(table_size_x, table_size_y)

gol_display.printTable(table)







