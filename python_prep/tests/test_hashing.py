#!/usr/bin/env python3

import unittest
from sources.hashing.hash_map import HashMap

class HashingTestCase(unittest.TestCase):

	def test_hash_map(self):
		keys = list(range(11, 100))
		items = list(zip(keys, keys))
		hash_map = HashMap(items)
		
		# Test len
		self.assertTrue(len(hash_map) == len(keys))

		# Test keys
		self.assertTrue(set(hash_map.keys) == set(keys))

		# Test values
		self.assertTrue(set(hash_map.values) == set(keys))

		# Test items
		self.assertTrue(set(hash_map.items) == set(items))

		# Test contains
		self.assertTrue(10 not in hash_map)

		# Test __setitem__
		hash_map[10] = 10
		self.assertTrue(len(hash_map) == len(keys) + 1)

		# Test iter, contains, and __getitem__
		for key, value in hash_map:
			self.assertTrue(key in hash_map)
			self.assertTrue(hash_map[key] == value)

		# Test __delitem__
		del hash_map[11]
		self.assertTrue(len(hash_map) == len(keys))
		self.assertTrue(11 not in hash_map)

		# Test insertion after deletion
		hash_map[1] = 1 
		self.assertTrue(len(hash_map) == len(keys) + 1)

		# Test contraction
		for key in range(12, 100):
			del hash_map[key]


if __name__ == '__main__':
    unittests.main()