
from enum import Enum 

class HashMethod(Enum):
	LINEAR_PROBING = "Linear probing"
	QUADRATIC_PROBING = "Quadratic probing"

class Dictionary(object):
	""" 
	Implementation of a dictionary data structure. 

	Currently uses linear probing.
	"""
	_DELETION_FLAG = '\n' # replace with enum?

	def __init__(self, hash_method, items=None):
		self._item_count = 0
		self._hash_method = hash_method

		if items is None:
			self._container_size = 8
			self._keys = [None for _ in range(self._container_size)]
			self._values = [None for _ in range(self._container_size)]
		else:
			# Avoid expansion operations
			self._container_size = self._next_power_of_2(len(items))
			self._new_keys_and_values(items)

	@property 
	def keys(self):
		return iter(x for x in self._keys if self._is_valid_item(x))

	@property 
	def values(self):
		return iter(x for x in self._values if self._is_valid_item(x))

	@property 
	def items(self):
		return iter(x for x in zip(self._keys, self._values) if self._is_valid_item(x[0]))

	def __iter__(self):
		return self.items

	def __len__(self):
		return self._item_count

	def __contains__(self, key):
		return self._search(key)

	def __getitem__(self, key):
		index = self._search(key)
		if index is not None:
			return self._values[index] 
		else:
			raise KeyError

	def __setitem__(self, key, value):
		self._insert_item(key, value)

	def __delitem__(self, key):
		""" 
		Replace the key's slot with a special flag indicating deletion. 

		Raises: 
			KeyError if the key is not in the dictionary.
		"""
		self._delete_item(key)

	def _is_valid_item(self, item):
		return item is not None and item != Dictionary._DELETION_FLAG

	def _search(self, key):
		""" 
		Return the index corresponding to the key.

		Amortized O(1) 
		"""

		for index in self._find_index(key):
			# skips special flag indicating deletion
			if self._keys[index] is None:
				return None
			if self._keys[index] == key:
				return index

	def _insert_item(self, key, value):
		""" Amortized Theta(1) """
		self._expand_container_if_necessary()

		for index in self._find_index(key):
			if self._keys[index] is None or self._keys[index] == Dictionary._DELETION_FLAG:
				self._item_count += 1
				self._keys[index] = key
				self._values[index] = value
				break

	def _delete_item(self, key):
		""" Amortized O(1) """
		self._contract_container_if_necessary()

		for index in self._find_index(key):
			if self._keys[index] is None:
				raise KeyError

			if self._keys[index] == key:
				self._item_count -= 1
				self._keys[index] = Dictionary._DELETION_FLAG
				self._values[index] = None
				break

	def _expand_container_if_necessary(self):
		""" Amortized Theta(1) """
		if self._item_count + 1 >= self._container_size:
			self._container_size *= 2
			self._new_keys_and_values(list(self.items))

	def _contract_container_if_necessary(self):
		""" Amortized O(1) """
		if self._item_count <= self._container_size / 4:
			self._container_size //= 2
			self._new_keys_and_values(list(self.items))

	def _new_keys_and_values(self, items):
		""" 
		Create new containers and insert the previous items into it.

		Best-case:
			Expansions not needed, no collisions occur
			Theta(n)
		Worst-case:
			Collision occurs on every insertion
			e.g. insert [0, 8, 16, 32 ...] 
			result of using linear probing
			Theta(n^2)
		"""
		self._item_count = 0

		self._keys = [None for _ in range(self._container_size)]
		self._values = [None for _ in range(self._container_size)]

		for key, value in items:
			self._insert_item(key, value)

	def _find_index(self, key):
		""" 
		Find the index corresponding to the key.

		Amortized O(1)
		"""
		if self._hash_method == HashMethod.LINEAR_PROBING:
			yield from self._find_index_using_linear_probing(key)
		else:
			yield from self._find_index_using_quadratic_probing(key)

	def _find_index_using_linear_probing(self, key):
		""" 
		Use linear probing to find the index corresponding to the key.

		Amortized O(1)

		Best-case:
			No collision
			Theta(1)
		Worst-case:
			Collision occurs and all subsequent slots are full, except last one
			Theta(n)
		"""
		hash_index = hash(key) % self._container_size
		
		left_half = list(range(hash_index))
		right_half = list(range(hash_index, self._container_size))
		
		indices = iter(right_half + left_half)

		while True:
			try:
				yield next(indices)
			except StopIteration:
				break

	def _find_index_using_quadratic_probing(self, key):
		""" 
		Use quadratic probing to find the index corresponding to the key.

		Amortized O(1)

		Best-case:
			No collision
			Theta(1)
		Worst-case:
			Collision occurs and all subsequent slots are full, except last one
			Theta(n)
		"""
		indices = iter(range(self._container_size))

		while True:
			try:
				yield (hash(key) + pow(next(indices),2)) % self._container_size
			except StopIteration:
				break

	def _next_power_of_2(self, n):
		n -= 1
		n |= n >> 1
		n |= n >> 2
		n |= n >> 4
		n |= n >> 8
		n |= n >> 16
		n += 1
		return n





