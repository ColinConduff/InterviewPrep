#!/usr/bin/env python3

import unittest
from collections import namedtuple
from sources.selection_algorithms.quick_select import *

class SelectionAlgorithmsTestCase(unittest.TestCase):

	def test_quick_select(self):
		Case = namedtuple('Case', ['seq', 'k', 'expected'])

		test_cases = [
			Case(seq=[1], k=1, expected=1),
			Case(seq=[3,1,2], k=1, expected=1),
			Case(seq=[3,1,2], k=2, expected=2),
			Case(seq=[3,1,2], k=3, expected=3)
		]

		for test_case in test_cases:
			observed = select(test_case.seq, test_case.k)
			self.assertTrue(observed == test_case.expected)

		sequence1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
		for k in sequence1:
			self.assertTrue(select(sequence1, k, in_place=True, check_sorted=True) == k)

		sequence2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
		for k in sequence2:
			self.assertTrue(select(sequence2, k, in_place=True, check_sorted=True) == k)

		sequence3 = [10, 5, 8, 7, 9, 6, 1, 3, 2, 4]
		for k in list(sequence3):
			self.assertTrue(select(sequence3, k, in_place=True, check_sorted=True) == k)


if __name__ == '__main__':
    unittests.main()