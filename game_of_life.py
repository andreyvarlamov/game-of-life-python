import gol_display
import random
import os
import time

# class for a cell
class Cell:
	pos_x = 0
	pos_y = 0
	alive = 1
	will_die = 0
	will_live = 0

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

		if cell.pos_y != 0:
			try:	
				neighbors.append(self.cells[cell.pos_x+1][cell.pos_y-1])
			except IndexError:
				None
	
			try:
				neighbors.append(self.cells[cell.pos_x][cell.pos_y-1])
			except IndexError:
				None


		if cell.pos_x != 0 and cell.pos_y != 0:
			try:
				neighbors.append(self.cells[cell.pos_x-1][cell.pos_y-1])
			except IndexError:
				None


		if cell.pos_x != 0:
			try:
				neighbors.append(self.cells[cell.pos_x-1][cell.pos_y])
			except IndexError:
				None
	
			try:
				neighbors.append(self.cells[cell.pos_x-1][cell.pos_y+1])
			except IndexError:
				None


		return neighbors

	def checkCell(self, cell):
		neighbors = self.neighbors(cell)
		result = 0
		neighbors_alive = 0 
		#underpopulation, normal, overpopulation, reproduction
		for neighbor in neighbors:
			if neighbor.alive == 1:
				neighbors_alive += 1

		if cell.alive == 1:
			if neighbors_alive < 2:
				cell.will_die = 1
			elif neighbors_alive > 3:
				cell.will_die = 1
			else:
				None
		else:
			if neighbors_alive == 3:
				cell.will_live = 1
			else: 
				None

	def processCell(self, cell):
		if cell.will_live == 1:
			cell.will_live = 0
			cell.live()

		if cell.will_die == 1:
			cell.will_die = 0
			cell.die()


	def process(self):
		for row in self.cells:
			for cell in row:
				self.checkCell(cell)

		for row in self.cells:
			for cell in row:
				self.processCell(cell)



table_size_x = 64
table_size_y = 64

table = Table(table_size_x, table_size_y)

iteration = 0
while True:
	os.system('cls')
	print("Generation " + str(iteration))
	gol_display.printTable(table)
	time.sleep(0.2)
	table.process()
	iteration += 1







