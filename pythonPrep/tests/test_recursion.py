#!/usr/bin/env python3

import unittest
from sources.recursion import *

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

if __name__ == '__main__':
    unittests.main()