#!/usr/bin/env python3

import unittest
from sources.sorting.quicksort import q_sort
from sources.sorting.mergesort import mergesort
from sources.sorting.insertion_sort import insertion_sort
from sources.sorting.counting_sort import counting_sort

class SortingTestCase(unittest.TestCase):

	# would use setup but most of these algorithms mutate the input sequence

	@staticmethod
	def _generate_testcases():
		return [
			[],
			[1],
			[2, 1],
			[10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
			[10, 1, 8, 3, 6, 4, 5, 7, 2, 9],
			[10, 10, 9, 9, 8, 8, 3, 3, 3, 3]
		]

	def test_quicksort(self):
		test_cases = self._generate_testcases()

		for test_case in test_cases:
			expected = sorted(test_case)
			observed = list(test_case)
			q_sort(observed)
			self.assertTrue(expected == observed)

	def test_mergesort(self):
		test_cases = self._generate_testcases()

		for test_case in test_cases:
			self.assertTrue(sorted(test_case) == mergesort(test_case))

	def test_insertion_sort(self):
		test_cases = self._generate_testcases()

		for test_case in test_cases:
			expected = sorted(test_case)
			observed = list(test_case)
			insertion_sort(observed)
			self.assertTrue(expected == observed)

	def test_counting_sort(self):
		test_cases = self._generate_testcases()

		for test_case in test_cases:
			expected = sorted(test_case)
			observed = list(test_case)
			counting_sort(observed)
			self.assertTrue(expected == observed)

		# test list containing str
		observed = ["d", "b", "c", "a"]
		expected = sorted(observed)
		counting_sort(observed)
		self.assertTrue(expected == observed)


if __name__ == '__main__':
    unittests.main()