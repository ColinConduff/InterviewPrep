
class HashMap(object):
	""" 
	Implementation of a hash map data structure. 

	Currently uses linear probing.
	"""

	def __init__(self, items=None):
		self._item_count = 0
		self._container_size = 8

		if items is None:
			self._keys = [None for _ in range(self._container_size)]
			self._values = [None for _ in range(self._container_size)]
		else:
			self._new_keys_and_values(items)

	@property 
	def keys(self):
		return iter(x for x in self._keys if x is not None)

	@property 
	def values(self):
		return iter(x for x in self._values if x is not None)

	@property 
	def items(self):
		return iter(x for x in zip(self._keys, self._values) if x[0] is not None)

	def __iter__(self):
		return self.items

	def __len__(self):
		return self._item_count

	def __contains__(self, key):
		return self._index_of(key) is not None

	def __getitem__(self, key):
		index = self._index_of(key)
		return self._values[index] if index is not None else None

	def __setitem__(self, key, value):
		self._insert_item(key, value)

	def _index_of(self, key):
		for index in self._find_index(key):
			if self._keys[index] is None:
				return None
			if self._keys[index] == key:
				return index

	def _new_keys_and_values(self, items):
		self._item_count = 0

		self._keys = [None for _ in range(self._container_size)]
		self._values = [None for _ in range(self._container_size)]

		for key, value in items:
			self._insert_item(key, value)

	def _insert_item(self, key, value):
		self._expand_container_if_necessary()

		for index in self._find_index(key):
			if self._keys[index] is None:
				self._item_count += 1
				self._keys[index] = key
				self._values[index] = value
				break

	def _expand_container_if_necessary(self):
		if self._item_count + 1 >= self._container_size:
			self._container_size *= 2
			self._new_keys_and_values(list(self.items))

	def _find_index(self, key):
		""" 
		Use linear probing to find the index corresponding to the key.

		Using the following iter might be more straightforward 
		iter(list(range(hash_index, _container_size)) + list(range(hash_index)))
		"""
		count = iter(range(self._container_size))
		index = hash(key) % self._container_size
		
		while True:
			yield index
			
			index += 1
			index %= self._container_size
			
			try:
				next(count)
			except StopIteration:
				break





