def printTable(table):	
	for index, row in enumerate(table.cells):
		for cell in row:
			if cell.alive == 1:
				print(chr(9632) + " ", end="")
			else:
				print("  ", end="")

		print('\n', end="")