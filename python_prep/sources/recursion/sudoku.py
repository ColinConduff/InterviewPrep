
# import numpy # uncomment to print grid
from collections import namedtuple

def solve_sudoku(grid):
	""" Return solved sudoku puzzle using brute force, recursive back-tracking method. """

	if len(grid) != 9 or len(grid[0]) != 9:
		raise Exception("Not a valid sudoku puzzle.")

	# Trade off size complexity for fast lookup
	LookupTable = namedtuple('LookupTable', ['row', 'col', 'square'])
	lookupTable = LookupTable(row=[set(row) for row in grid], 
				         col=[set(col) for col in zip(*grid)], 
			             square=[set() for _ in range(9)]) 

	_setup_lookup_square(grid, lookupTable)
	
	if not _sudoku_puzzle_is_solved(grid, lookupTable):
		raise Exception("No solution found.")
	
	# print(numpy.matrix(grid))
	return grid

def _sudoku_puzzle_is_solved(grid, lookupTable, row=0, col=0):
	""" Side effect: solves sudoku puzzle """

	if _last_position_is_filled(grid):
		return True

	# Should skip if the value was placed initially
	while grid[row][col] != 0:
		row, col = _next_cell(row, col)

	for num in range(1, 10):

		if not _conflict_exists(lookupTable, row, col, num):

			_add(grid, lookupTable, num, row, col)

			next_row, next_col = _next_cell(row, col)

			if _sudoku_puzzle_is_solved(grid, lookupTable, next_row, next_col):
				return True

			_remove(grid, lookupTable, num, row, col)

	return False

def _next_cell(row, col):
	next_col = col + 1
	next_row = row

	if next_col > 8:
		next_col = 0
		next_row += 1

	return (next_row, next_col)

def _last_position_is_filled(grid):
	last_row = len(grid) - 1
	last_col = len(grid[0]) - 1
	return grid[last_row][last_col] != 0

def _add(grid, lookupTable, num, row, col):
	grid[row][col] = num
	lookupTable.row[row].add(num)
	lookupTable.col[col].add(num)
	lookupTable.square[_square_num(row, col)].add(num)

def _remove(grid, lookupTable, num, row, col):
	grid[row][col] = 0
	lookupTable.row[row].remove(num)
	lookupTable.col[col].remove(num)
	lookupTable.square[_square_num(row, col)].remove(num)

def _conflict_exists(lookupTable, row, col, num):

	return (num in lookupTable.row[row] or \
		    num in lookupTable.col[col] or \
		    num in lookupTable.square[_square_num(row, col)])

def _square_num(row, col):
	if 0 <= row < 3:
		if 0 <= col < 3:
			return 0
		elif 3 <= col < 6:
			return 1
		elif 6 <= col < 9:
			return 2
	elif 3 <= row < 6:
		if 0 <= col < 3:
			return 3
		elif 3 <= col < 6:
			return 4
		elif 6 <= col < 9:
			return 5
	elif 6 <= row < 9:
		if 0 <= col < 3:
			return 6
		elif 3 <= col < 6:
			return 7
		elif 6 <= col < 9:
			return 8

def _setup_lookup_square(grid, lookupTable):
	for row in grid[:3]:
		for num in row[:3]:
			lookupTable.square[0].add(num)
		for num in row[3:6]:
			lookupTable.square[1].add(num)
		for num in row[6:9]:
			lookupTable.square[2].add(num)

	for row in grid[3:6]:
		for num in row[:3]:
			lookupTable.square[3].add(num)
		for num in row[3:6]:
			lookupTable.square[4].add(num)
		for num in row[6:9]:
			lookupTable.square[5].add(num)

	for row in grid[6:9]:
		for num in row[:3]:
			lookupTable.square[6].add(num)
		for num in row[3:6]:
			lookupTable.square[7].add(num)
		for num in row[6:9]:
			lookupTable.square[8].add(num)

