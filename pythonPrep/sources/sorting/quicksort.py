import random

def q_sort(sequence):
	""" Return a sequence sorted in ascending order. """
	quicksort(sequence, 0, len(sequence) - 1)

def quicksort(sequence, left_index, right_index):
	""" 
	Recursively partition subsequences around randomly selected pivot 
		values until the sequence is sorted in ascending order.

	Time Complexity: 
		Omega(n log(n)) 
			[Comparison sort lower-bound]
		O(n^2) 
			[if the randomly selected pivot values are the min or max of 
					the current subsequence]
	Space Complexity:
		O(log(n))
	Discussion:
		Not Stable
		In-Place
		Typically faster in practice than merge-sort
	Args: 
		sequence: A list to be mutated and sorted in place.
		left_index: The farthest left index of the subsequence to sort.
		right_index: The farthest right index of the subsequence to sort.
	Returns:
		sequence
	"""
	if len(sequence) <= 1 or left_index >= right_index:
		return
	
	pivot_index = random.randrange(left_index, right_index)
	new_pivot_index = partition(sequence, left_index, right_index, pivot_index)

	quicksort(sequence, left_index, new_pivot_index - 1)
	quicksort(sequence, new_pivot_index + 1, right_index)

def partition(sequence, left_index, right_index, pivot_index):
	""" 
	Move values less than the pivot value to the left of the pivot index.
	
	Args: 
		sequence: A list to be mutated and sorted in place.
		left_index: The farthest left index of the subsequence to sort.
		right_index: The farthest right index of the subsequence to sort.
		pivot_index: The index of the value to partition the subsequence around.
	Returns:
		The index which partitions smaller values to the left and larger values to the right.
	"""
	pivot_value = sequence[pivot_index]
	sequence[pivot_index], sequence[right_index] = sequence[right_index], sequence[pivot_index]
	new_pivot_index = left_index

	for current_index in range(left_index, right_index):
		if sequence[current_index] < pivot_value:
			sequence[current_index], sequence[new_pivot_index] = \
				sequence[new_pivot_index], sequence[current_index]
			new_pivot_index += 1

	sequence[new_pivot_index], sequence[right_index] = sequence[right_index], sequence[new_pivot_index]
	return new_pivot_index
		
