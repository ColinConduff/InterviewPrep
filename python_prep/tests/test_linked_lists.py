#!/usr/bin/env python3

import unittest
from sources.linked_lists.singly_linked_list import SinglyLinkedList
from sources.linked_lists.doubly_linked_list import DoublyLinkedList

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

	def test_doubly_linked_list(self):
		dll = DoublyLinkedList()

		# Test initial list
		self.assertTrue(len(dll) == 0)

		# Test insertion at index=0
		dll.insert(3)
		dll.insert(2)
		dll.insert(1)

		self.assertTrue(len(dll) == 3)
		self.assertTrue(dll == [1, 2, 3])
		self.assertTrue(dll._tail.data == 3)

		# Test insertion at last index 
		dll.insert(5, len(dll))
		dll.insert(6, len(dll))
		self.assertTrue(dll._tail.data == 6)

		# Test insertion at an interior index
		dll.insert(4, 3)
		self.assertTrue(dll._tail.data == 6)

		self.assertTrue(len(dll) == 6)
		self.assertTrue(dll == [1, 2, 3, 4, 5, 6])
		self.assertTrue(dll._tail.data == 6)

		# Test pop when index == 0
		self.assertTrue(dll.pop(0) == 1)
		self.assertTrue(len(dll) == 5)

		# Test pop last index
		popped = dll.pop(len(dll) - 1)

		self.assertTrue(popped == 6)
		self.assertTrue(len(dll) == 4)

		# Test pop interior index
		self.assertTrue(dll.pop(1) == 3)
		self.assertTrue(len(dll) == 3)

		self.assertTrue(dll == [2, 4, 5])

	def test_bubble_sort_on_doubly_linked_list(self):
		list_to_sort = [5,2,8,4,7,9,1,3,10,6]
		dll = self._dll_for_sorting(list_to_sort)
		dll.bubble_sort()
		self.assertTrue(dll == sorted(list_to_sort))

	def test_insertion_sort_on_doubly_linked_list(self):
		list_to_sort = [5,2,8,4,7,9,1,3,10,6]
		dll = self._dll_for_sorting(list_to_sort)
		dll.insertion_sort()
		self.assertTrue(dll == sorted(list_to_sort))

	def _dll_for_sorting(self, list_to_sort):
		dll = DoublyLinkedList()
		for num in list_to_sort:
			dll.insert(num)
		return dll


if __name__ == '__main__':
    unittests.main()