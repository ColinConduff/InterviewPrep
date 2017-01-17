#!/usr/bin/env python3

import unittest
from sources.dynamic_algs.lcs import *

class DynamicAlgsTestCase(unittest.TestCase):

	def test_longest_common_substring(self):
		test_cases = [
			("something", "home", "ome"),
			("home", "something", "ome"),
			("something", "", ""),
			("abcdefg", "abceg", "abc")
		]

		for test_case in test_cases:
			observed = longest_common_substring(test_case[0], test_case[1])
			expected = test_case[2]
			self.assertTrue(observed == expected)

	def test_longest_common_subsequence(self):
		test_cases = [
			("something", "home", "ome"),
			("home", "something", "ome"),
			("something", "", ""),
			("abcdefg", "abceg", "abceg")
		]

		for test_case in test_cases:
			observed = longest_common_subsequence(test_case[0], test_case[1])
			expected = test_case[2]
			self.assertTrue(observed == expected)

if __name__ == '__main__':
    unittests.main()