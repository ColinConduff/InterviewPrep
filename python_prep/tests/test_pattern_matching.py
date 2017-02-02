#!/usr/bin/env python3

import unittest
from sources.pattern_matching.knuth_morris_pratt import kmp

class PatternMatchingTestCase(unittest.TestCase):

	def test_kmp(self):
		test_cases = [
			("abc", "abcabc", 0),
			("abcdabd", "abcabcdababcdabcdabde", 13)
		]

		for test_case in test_cases:
			observed = kmp(test_case[0], test_case[1])
			expected = test_case[2]
			self.assertTrue(observed == expected)

if __name__ == '__main__':
    unittests.main()