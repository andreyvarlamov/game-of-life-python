def printTable(table):	
	for index, row in enumerate(table.cells):
		for cell in row:
			print(str(cell.alive) + " ", end="")

		print('\n', end="")