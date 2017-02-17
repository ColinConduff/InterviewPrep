
import io

from sources.linked_lists.singly_linked_list import LinkedListIter

""" TODO: make LinkedList base class """

class Node(object):
	def __init__(self, data, prev=None, next=None):
		self.data = data
		self.prev = prev 
		self.next = next

	def __str__(self):
		return str(self.data)

class DoublyLinkedList(object):

	def __init__(self):
		self._head = None
		self._tail = None
		self._size = 0 # move to base class

	def __len__(self): # move to base class
		return self._size

	def __eq__(self, other): # move to base class
		if type(other) is type(self) or type(other) is list:
			return self._is_equal_to_list(other)
		else:
			return False

	def __iter__(self): # move to base class
		""" Encapsulate access to _head when making iter. """
		return LinkedListIter(self._head)

	def __str__(self): # move to base class
		output = io.StringIO()

		self_iter = iter(self)
		while True:
			try:
				output.write("{} ".format(next(self_iter)))
			except StopIteration:
				break

		content = output.getvalue()
		output.close()

		return content

	def insert(self, data, index=0):
		if index < 0 or index > self._size:
			raise IndexError

		if self._head is None:
			self._head = Node(data)
			self._tail = self._head

		elif index == 0:
			self._head = Node(data, next=self._head)
			self._head.next.prev = self._head

		elif index == self._size:
			previous_tail = self._tail
			self._tail = Node(data, prev=previous_tail, next=None)
			previous_tail.next = self._tail

		else:
			position = 1
			node = self._head

			while position != index:
				node = node.next
				position += 1

			node.next = Node(data, prev=node, next=node.next)

		self._size += 1

	def pop(self, index):
		if index < 0 or index >= self._size:
			raise IndexError

		if self._size == 1:
			node_to_return = self._head
			self._head = None
			self._tail = None

		elif index == 0:
			node_to_return = self._head
			self._head = self._head.next
			self._head.prev = None

		elif index == self._size - 1:
			node_to_return = self._tail
			self._tail = self._tail.prev
			self._tail.next = None

		else:
			position = 1
			node = self._head

			while position != index:
				node = node.next
				position += 1

			node_to_return = node.next

			# node.next.next cannot be None
			node.next.next.prev = node
			node.next = node.next.next

		self._size -= 1
		return node_to_return.data
			
	def bubble_sort(self):
		if self._head is None:
			return 

		for _ in range(self._size):
			swaps_made = 0
			node = self._head.next

			while node is not None:
				if node.prev.data > node.data:
					swaps_made += 1
					node.prev.data, node.data = node.data, node.prev.data

				node = node.next

			if swaps_made == 0:
				break

	def insertion_sort(self):
		if self._head is None:
			return

		advancing = self._head.next

		while advancing is not None:
			key = advancing.data
			retreating = advancing.prev

			while retreating is not None and retreating.data > key:
				retreating.next.data = retreating.data
				retreating = retreating.prev

			if retreating is None:
				self._head.data = key
			else:
				retreating.next.data = key

			advancing = advancing.next

	# Not used but may be necessary
	def _swap(self, previous, current, next):
		if previous == self._head:
			self._head = current
		else:
			previous.prev.next = current

		if current == self._tail:
			self._tail = previous
		else:
			next.prev = previous

		current.next = previous
		current.prev = previous.prev
		previous.prev = current
		previous.next = next

	def _is_equal_to_list(self, other):
		""" 
		Return True if the two lists are equivalent.

		The two lists are equivalent if they have the same lengths and contain 
			the same items in the same order.
		"""
		if len(other) != len(self):
			return False

		if type(other) is list:
			other_iter = iter(other)
		else:
			other_iter = iter(other)

		self_iter = iter(self)

		while True:
			try:
				if next(self_iter) != next(other_iter):
					return False
			except StopIteration:
				break

		return True
