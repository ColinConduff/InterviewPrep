import random

def select(sequence, k, in_place=False, check_sorted=False):
	"""
	Select the kth smallest element in the sequence.

	Args:
		sequence: 
			A list of comparable elements.
		k: 
			An integer. 
			If k == 1, return smallest element in list.
			Valid k values: [1, len(sequence)].
		in_place: 
			If true, the sequence is mutated / partially sorted.
		check_sorted: 
			If true, checks if the sequence is sorted in ascending 
				or descending order.

	Returns:
		The kth smallest element in the sequence.

	Raises:
		Exception if k <= 0 or k > len(sequence)

	Discussion: 
		If in_place == True, then the input sequence may eventually become sorted.
		If check_sorted == True, the time complexity remains O(n).
		If the sequence is sorted, it is slightly faster to check if it is sorted
			and return the kth element, rather than use quick select.
	"""
	if not (0 < k <= len(sequence)):
		raise Exception("Invalid k value. Valid k value: 0 < k <= len(sequence)")

	k_index = k - 1

	# If the sequence is already sorted, just return the kth element.
	if check_sorted:
		if is_sorted(sequence): # ascending 
			return sequence[k_index]
		if is_sorted(sequence, lambda x, y: x >= y): # descending
			return sequence[len(sequence) - k]

	if not in_place:
		sequence = list(sequence)

	return quick_select(sequence, 0, len(sequence) - 1, k_index)

def quick_select(sequence, left_index, right_index, k_index):
	""" 
	Use quick select algorithm to find the kth smallest element. 
	Time: O(n)
	Space: O(log(n))
	"""
	if len(sequence) <= 1 or left_index == right_index:
		return sequence[k_index]

	elif left_index < right_index:
		pivot_index = random.randrange(left_index, right_index) # Make worst-case unlikely
		new_pivot_index = partition(sequence, left_index, right_index, pivot_index)

		if k_index < new_pivot_index:
			return quick_select(sequence, left_index, new_pivot_index - 1, k_index)
		elif k_index > new_pivot_index:
			return quick_select(sequence, new_pivot_index + 1, right_index, k_index)
		else:
			return sequence[k_index]

def partition(sequence, left_index, right_index, pivot_index):
	""" 
	Partition the sequence such that items less than the pivot are to the left of it. 
	"""
	pivot_value = sequence[pivot_index]
	sequence[pivot_index], sequence[right_index] = sequence[right_index], sequence[pivot_index]
	new_pivot_index = left_index

	for c_index in range(left_index, right_index):
		if sequence[c_index] < pivot_value:
			sequence[new_pivot_index], sequence[c_index] = sequence[c_index], sequence[new_pivot_index]
			new_pivot_index += 1

	sequence[new_pivot_index], sequence[right_index] = sequence[right_index], sequence[new_pivot_index]
	return new_pivot_index

def is_sorted(sequence, order=lambda x, y: x <= y):
	""" 
	Returns True if "order" returns true for all pairs of items in the sequence.
	Time: O(n) 
	""" 
	for n in range(1, len(sequence)):
		if not order(sequence[n-1], sequence[n]):
			return False
	return True


