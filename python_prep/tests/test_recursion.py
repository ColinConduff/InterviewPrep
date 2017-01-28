#!/usr/bin/env python3

import unittest
from sources.recursion.misc_recursion import *
from sources.recursion.sudoku import *

class RecursionTestCase(unittest.TestCase):

	def test_power_of(self):
		powers_of_two = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

		for index in range(11):
			solution = powers_of_two[index]
			self.assertTrue(power_of(2, index) == solution)

	def test_is_palindrome(self):
		self.assertTrue(is_palindrome("lol", 0, 2))
		self.assertFalse(is_palindrome("lolo", 0, 3))

	def test_binary_search(self):
		sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

		for num in sequence:
			self.assertTrue(binary_search(sequence, num) == num)

		self.assertTrue(binary_search(sequence, 20) == None)
		self.assertTrue(binary_search([], 0) == None)
		self.assertTrue(binary_search([0], 0) == 0)

	def test_choose(self):
		self.assertTrue(choose(10, 1) == 10)
		self.assertTrue(choose(10, 10) == 1)

	def test_towers_of_hanoi(self):
		for n in range(1, 4):
			towers = towers_of_hanoi(n)
			self.assertTrue(len(towers[0]) == 0)
			self.assertTrue(len(towers[1]) == n)
			self.assertTrue(len(towers[2]) == 0)

	def test_permutations(self):
		self.assertTrue(permutations("abc") == {'abc', 'acb', 'cab', 'cba', 'bca', 'bac'})

	def test_fibonacci(self):
		fib_sequence = [1, 1, 2, 3, 5, 8, 13]

		for i, n in enumerate(fib_sequence):
			self.assertTrue(naive_fib(i+1) == n)
			self.assertTrue(dyn_fib(i+1) == n)

	def test_subsets(self):
		self.assertTrue(subsets("abc") == {'', 'ac', 'b', 'c', 'abc', 'ab', 'bc', 'a'})

	def test_place_queens(self):
		expected = {(0,0)}
		observed = place_queens(1, 1)
		self.assertTrue(observed == expected)

		expected = set()
		observed = place_queens(2, 2)
		self.assertTrue(observed == expected)

		expected = set()
		observed = place_queens(3, 3)
		self.assertTrue(observed == expected)

		expected = {(2, 3), (1, 0), (3, 1), (0, 2)}
		observed = place_queens(4, 4)
		self.assertTrue(observed == expected)

	def test_solve_sudoku(self):
		observed = [
			[0, 0, 0,  0, 0, 0,  6, 8, 0],
			[0, 0, 0,  0, 7, 3,  0, 0, 9],
			[3, 0, 9,  0, 0, 0,  0, 4, 5],

			[4, 9, 0,  0, 0, 0,  0, 0, 0],
			[8, 0, 3,  0, 5, 0,  9, 0, 2],
			[0, 0, 0,  0, 0, 0,  0, 3, 6],

			[9, 6, 0,  0, 0, 0,  3, 0, 8],
			[7, 0, 0,  6, 8, 0,  0, 0, 0],
			[0, 2, 8,  0, 0, 0,  0, 0, 0]
		] 

		expected = [
			[1, 7, 2,  5, 4, 9,  6, 8, 3],
			[6, 4, 5,  8, 7, 3,  2, 1, 9],
			[3, 8, 9,  2, 6, 1,  7, 4, 5],

			[4, 9, 6,  3, 2, 7,  8, 5, 1],
			[8, 1, 3,  4, 5, 6,  9, 7, 2],
			[2, 5, 7,  1, 9, 8,  4, 3, 6],

			[9, 6, 4,  7, 1, 5,  3, 2, 8],
			[7, 3, 1,  6, 8, 2,  5, 9, 4],
			[5, 2, 8,  9, 3, 4,  1, 6, 7]
		]

		solve_sudoku(observed)

		self.assertTrue(expected == observed)

if __name__ == '__main__':
    unittests.main()