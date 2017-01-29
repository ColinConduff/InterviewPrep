#!/usr/bin/env python3

import unittest
from sources.hashing.hash_map import HashMap

class HashingTestCase(unittest.TestCase):

	def test_hash_map(self):
		keys = [1,2,3,4,5,6,7,8,9]
		items = list(zip(keys, keys))
		hash_map = HashMap(items)
		
		self.assertTrue(len(hash_map) == 9)
		self.assertTrue(set(hash_map.keys) == set(keys))
		self.assertTrue(set(hash_map.values) == set(keys))
		self.assertTrue(set(hash_map.items) == set(items))

		self.assertTrue(10 not in hash_map)
		hash_map[10] = 10
		self.assertTrue(len(hash_map) == 10)

		for key, value in hash_map:
			self.assertTrue(key in hash_map)
			self.assertTrue(hash_map[key] == value)


if __name__ == '__main__':
    unittests.main()