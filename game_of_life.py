# class for a cell
class Cell:
	pos_x = 0
	pos_y = 0
	alive = 1

	def __init__(self, pos_x , pos_y, alive):
		pass

	def die(self):
		alive = 0

class Table:
	cells = []

	def __init__(self, size_x, size_y):
		generateCells(size_x, size_y)


	def generateCells(self, size_x, size_y):
		for i in range(0, table_size_x):
			cell_row = []
			for j in range(0, table_size_y):
				cell_row.append(Cell(i, j, 0))\

			cells.append(cell_row)

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

class Game:
	table_size_x = 64
	table_size_y = 64







