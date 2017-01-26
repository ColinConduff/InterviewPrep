#!/usr/bin/env python3

"""
Adapted from Stanford Programming Abstractions Course 
"""

def power_of(base, exp):
	if exp < 0:
		raise Exception("Exponent must be >= 0.") 
	elif exp == 0:
		return 1
	else:
		return base * power_of(base, exp - 1)

def is_palindrome(p_str, left_index, right_index):
	if left_index >= right_index:
		return True
	elif p_str[left_index] != p_str[right_index]:
		return False
	else:
		return is_palindrome(p_str, left_index+1, right_index-1)

def _binary_search(sequence, key, left_index, right_index):

	if left_index > right_index:
		return None

	middle_index = left_index + (right_index - left_index) // 2

	if key < sequence[middle_index]:
		return _binary_search(sequence, key, left_index, middle_index - 1)
	elif key > sequence[middle_index]:
		return _binary_search(sequence, key, middle_index + 1, right_index)
	else:
		return middle_index

def binary_search(sequence, key):
	return _binary_search(sequence, key, 0, len(sequence) - 1)

def choose(n, k):
	""" 
	N-choose-K C(n,k), 
	Given N items, how many ways can you choose K of them.
	
	Base Case: 
	No choices remaining ( k == n)
	k == 0
	
	Number of subsets that include item 1 = C(n-1, k-1)
	+ Number of subsets that do not include item 1 = C(n-1, k)
	"""
	if n < 0 or k < 0:
		raise Exception("n >= k > 0")
	elif k == 0 or k == n:
		return 1
	else:
		return choose(n-1, k) + choose(n-1, k-1)

def _move_tower(n, src, dst, tmp):
	if n <= 0:
		return

	_move_tower(n - 1, src, tmp, dst)
	dst.append(src.pop())
	_move_tower(n - 1, tmp, dst, src)

def towers_of_hanoi(n):
	towers = [
		list(reversed(range(n))),
		[],
		[]
	]

	_move_tower(n, towers[0], towers[1], towers[2])

	return towers

def _permute(current, letters, output):
	"""
	Time: O(!n)
	"""
	if len(letters) == 0:
		output.add(current)
	else:
		for letter_index, letter in enumerate(letters):
			next = current + letter
			remaining = letters - set(letter)
			_permute(next, remaining, output) # called n times

def permutations(letters):
	output = set()
	letters = set(list(letters))
	_permute("", letters, output)
	return output

def naive_fib(n):
	"""
	Time: O(2^n)

	Compare to dynamic approach with Time: O(n)
	"""
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return naive_fib(n-1) + naive_fib(n-2)

def dyn_fib(n, i=1, next=1, current=1):
	""" Time: O(n) """
	if i == n:
		return current

	return dyn_fib(n, i+1, next+current, next)

def _subsets(remaining, subset, output):
	""" Time: O(2^n) """
	if len(remaining) == 0:
		output.add(subset)
	else:
		_subsets(remaining[1:], subset + remaining[0], output)
		_subsets(remaining[1:], subset, output)

def subsets(string):
	output = set()
	_subsets(string, "", output)
	return output

def _diagonal_is_safe(max_row, max_col, row, col, placed_queens, mod_cell):
	d_row = row
	d_col = col
	while d_row >= 0 and d_col >= 0 and \
		d_row < max_row and d_col < max_col:

		if (d_row, d_col) in placed_queens:
			return False

		d_row, d_col = mod_cell(d_row, d_col)

	return True

def _is_safe(max_row, max_col, row, col, placed_queens):
	""" Time: O(max_row + max_col) """
	for q_row, q_col in placed_queens:
		if row == q_row or q_col == col:
			return False

	upper_right = lambda r, c: (r - 1, c + 1)
	upper_left = lambda r, c: (r - 1, c - 1)
	lower_right = lambda r, c: (r + 1, c + 1)
	lower_left = lambda r, c: (r + 1, c - 1)

	diagonals = [upper_right, upper_left, lower_right, lower_left]

	for diagonal in diagonals:
		if not _diagonal_is_safe(max_row, max_col, row, col, placed_queens, diagonal):
			return False

	return True

def _did_place_all_queens(max_row, max_col, placed_queens, col=0):
	""" Side effect: mutates placed_queens """

	if col >= max_col:
		return True

	for row in range(max_row):
		if _is_safe(max_row, max_col, row, col, placed_queens): # O(max_row + max_col)
			placed_queens.add((row, col))

			if _did_place_all_queens(max_row, max_col, placed_queens, col+1):
				return True

			placed_queens.remove((row, col))

	return False

def place_queens(max_row, max_col):
	""" 
	Recursion Back-Tracking Example

	Find (row, col) for queens such that they are not
		on the same row, column, or diagonal.

	note: (0,0) is top left on board 
	"""
	placed_queens = set()
	_did_place_all_queens(max_row, max_col, placed_queens)
	return placed_queens

# if __name__ == '__main__':
