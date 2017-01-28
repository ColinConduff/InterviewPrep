import io

class Node(object):
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data)

class LinkedListIter(object):
	"""Iterator for looping over a linked list."""
	def __init__(self, node):
		self.node = node

	def __iter__(self):
		return self

	def __next__(self):
		current_node = self.node
		
		if current_node is None:
			raise StopIteration
		
		self.node = current_node.next
		return current_node.data

class SinglyLinkedList(object):

	def __init__(self):
		self._head = None
		self._size = 0

	def __len__(self):
		return self._size

	def __str__(self):
		output = io.StringIO()

		self_iter = self.iterator
		while True:
			try:
				output.write("{} ".format(next(self_iter)))
			except StopIteration:
				break

		content = output.getvalue()
		output.close()

		return content

	def __getitem__(self, index):
		""" Return the data corresponding to the node at the given index. """
		return self._node_previous_to(index).next.data # raises appropriate error

	def __eq__(self, other):
		if type(other) is type(self) or type(other) is list:
			return self._is_equal_to_list(other)
		else:
			return False

	@property 
	def iterator(self):
		""" Encapsulate access to _head when making iter. """
		return LinkedListIter(self._head)

	def insert(self, data, index=0):
		""" 
		Insert an item at an index. 

		Raises:
			IndexError
		"""
		if not (0 <= index <= self._size):
			raise IndexError

		self._size += 1

		if self._head is None:
			self._head = Node(data)
		
		elif index == 0:
			self._head = Node(data, self._head)

		else:
			node = self._node_previous_to(index)
			node.next = Node(data, node.next)

	def pop(self, index=0):
		"""
		Return the item at the given index and remove it from the list.

		Raises:
			IndexError
		"""
		if not (0 <= index < self._size):
			raise IndexError

		if index == 0:
			item_to_pop = self._head
			self._head = self._head.next

		else:
			node = self._node_previous_to(index)
			item_to_pop = node.next 
			node.next = node.next.next

		self._size -= 1

		return item_to_pop.data

	def reverse(self):
		""" Reverse the linked list in place. """

		if self._size <= 1:
			return

		previous_node = self._head
		current_node = self._head.next

		previous_node.next = None

		while current_node is not None:
			next_node = current_node.next 
			current_node.next = previous_node

			previous_node = current_node
			current_node = next_node

		self._head = previous_node

	@property 
	def is_palindrome(self):
		""" 
		1. Reverse second half of list.  
		2. Iterate from the left and right at the same time and check for equality.
		"""
		pass

	@property
	def contains_cycle(self):
		""" Check for equality of slow runner and fast runner (assumes unique data items). """
		pass

	def _node_previous_to(self, index):
		""" Return the node previous to the given index. """
		
		if not (0 < index < self._size):
			raise IndexError

		position = 1
		node = self._head

		while node is not None and position != index:
			node = node.next
			position += 1

		return node

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
			other_iter = other.iterator

		self_iter = self.iterator

		while True:
			try:
				if next(self_iter) != next(other_iter):
					return False
			except StopIteration:
				break

		return True


