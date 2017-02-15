#!/usr/bin/env python3

import unittest
from sources.linked_lists.singly_linked_list import SinglyLinkedList

class LinkedListTestCase(unittest.TestCase):

	def test_singly_linked_list(self):
		ssl = SinglyLinkedList()

		# Test initial list
		self.assertTrue(len(ssl) == 0)
		self.assertTrue(ssl == [])

		# Test insertion at index=0
		ssl.insert(3)
		ssl.insert(2)
		ssl.insert(1)

		self.assertTrue(len(ssl) == 3)
		self.assertTrue(ssl == [1, 2, 3])

		# Test insertion at last index 
		ssl.insert(5, len(ssl))
		ssl.insert(6, len(ssl))

		# Test insertion at an interior index
		ssl.insert(4, 3)

		self.assertTrue(len(ssl) == 6)
		self.assertTrue(ssl == [1, 2, 3, 4, 5, 6])

		# Test pop when index == 0
		self.assertTrue(ssl.pop() == 1)
		self.assertTrue(len(ssl) == 5)

		# Test pop last index
		self.assertTrue(ssl.pop(len(ssl) - 1) == 6)
		self.assertTrue(len(ssl) == 4)

		# Test pop interior index
		self.assertTrue(ssl.pop(1) == 3)
		self.assertTrue(len(ssl) == 3)

		self.assertTrue(ssl == [2, 4, 5])

		# Test ssl comparison
		duplicate_ssl = SinglyLinkedList()
		duplicate_ssl.insert(5)
		duplicate_ssl.insert(4)
		duplicate_ssl.insert(2)

		self.assertTrue(duplicate_ssl == ssl)

		ssl.reverse()
		self.assertTrue(ssl == [5, 4, 2])

	def test_ssl_contains_cycle(self):
		ssl = SinglyLinkedList()
		ssl.insert(1, len(ssl))
		ssl.insert(2, len(ssl))

		self.assertFalse(ssl.contains_cycle)

		ssl.insert(3, len(ssl))
		ssl.insert(4, len(ssl))

		self.assertFalse(ssl.contains_cycle)

		ssl._head.next.next.next = ssl._head.next

		self.assertTrue(ssl.contains_cycle)

		ssl._head.next = ssl._head

		self.assertTrue(ssl.contains_cycle)



if __name__ == '__main__':
    unittests.main()