#!/usr/bin/env python3

import unittest
from sources.hashing.dictionary import HashMethod
from sources.hashing.dictionary import Dictionary

class HashingTestCase(unittest.TestCase):

	def test_dictionary_linear_probing(self):
		keys = list(range(11, 100))
		items = list(zip(keys, keys))
		hash_method = HashMethod.LINEAR_PROBING
		dictionary = Dictionary(hash_method, items)
		
		# Test len
		self.assertTrue(len(dictionary) == len(keys))

		# Test keys
		self.assertTrue(set(dictionary.keys) == set(keys))

		# Test values
		self.assertTrue(set(dictionary.values) == set(keys))

		# Test items
		self.assertTrue(set(dictionary.items) == set(items))

		# Test contains
		self.assertTrue(10 not in dictionary)

		# Test __setitem__
		dictionary[10] = 10
		self.assertTrue(len(dictionary) == len(keys) + 1)

		# Test iter, contains, and __getitem__
		for key, value in dictionary:
			self.assertTrue(key in dictionary)
			self.assertTrue(dictionary[key] == value)

		# Test __delitem__
		del dictionary[11]
		self.assertTrue(len(dictionary) == len(keys))
		self.assertTrue(11 not in dictionary)

		# Test insertion after deletion
		dictionary[1] = 1 
		self.assertTrue(len(dictionary) == len(keys) + 1)

		# Test contraction
		for key in range(12, 100):
			del dictionary[key]

	def test_dictionary_quadratic_probing(self):
		keys = list(range(11, 100))
		items = list(zip(keys, keys))
		hash_method = HashMethod.QUADRATIC_PROBING
		dictionary = Dictionary(hash_method, items)
		
		# Test len
		self.assertTrue(len(dictionary) == len(keys))

		# Test keys
		self.assertTrue(set(dictionary.keys) == set(keys))

		# Test values
		self.assertTrue(set(dictionary.values) == set(keys))

		# Test items
		self.assertTrue(set(dictionary.items) == set(items))

		# Test contains
		self.assertTrue(10 not in dictionary)

		# Test __setitem__
		dictionary[10] = 10
		self.assertTrue(len(dictionary) == len(keys) + 1)

		# Test iter, contains, and __getitem__
		for key, value in dictionary:
			self.assertTrue(key in dictionary)
			self.assertTrue(dictionary[key] == value)

		# Test __delitem__
		del dictionary[11]
		self.assertTrue(len(dictionary) == len(keys))
		self.assertTrue(11 not in dictionary)

		# Test insertion after deletion
		dictionary[1] = 1 
		self.assertTrue(len(dictionary) == len(keys) + 1)

		# Test contraction
		for key in range(12, 100):
			del dictionary[key]


if __name__ == '__main__':
    unittests.main()