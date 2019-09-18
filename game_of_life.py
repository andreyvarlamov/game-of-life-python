import gol_display
import gol_gui
import random
import os
import time

# # class for a cell
# class Cell:
# 	posX = 0
# 	posY = 0
# 	alive = 0

# 	def __init__(self, posX , posY, alive):
# 		self.posX = posX
# 		self.posY = posY
# 		self.alive = alive

# 	def die(self):
# 		self.alive = 0

# 	def live(self):
# 		self.alive = 1

class Table:
	def __init__(self, size):
		self.size = size
		self.generateCells()


	def generateCells(self, empty=1):
		if empty:
			self.cells = [[[0,0] for x in range(self.size)] for y in range(self.size)]
		else:
			randInt = random.randint(0,1)
			self.cells = [[[randInt,randInt] for x in range(self.size)] for y in range(self.size)]


	def countNeighbors(self, x, y):
		neighborCount = 0
		neighborOffsets = [(1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1), (0,-1), (1,-1)]

		for offset in neighborOffsets:
			try:
				if self.cells[x + offset[0]][y + offset[1]][0] == 1:
					neighborCount += 1
			except IndexError:
				None


		return neighborCount


	def checkCell(self, x, y):
		neighborCount = self.countNeighbors(x, y)

		if self.cells[x][y][0] == 1:
			if neighborCount < 2 or neighborCount > 3:
				self.cells[x][y][1] = 0
			else:
				self.cells[x][y][1] = 1


		else:
			if neighborCount == 3:
				self.cells[x][y][1] = 1
			else:
				self.cells[x][y][1] = 0

		
	def processCell(self, x, y):
		self.cells[x][y][0] = self.cells[x][y][1]


	def process(self):
		for x in range(self.size):
			for y in range(self.size):
				self.checkCell(x, y)

			
		for x in range(self.size):
			for y in range(self.size):
				self.processCell(x, y)

			




table_size = 50

table = Table(table_size)

gameGui = gol_gui.GameGui(table)









