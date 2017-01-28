
def mergesort(sequence):
	""" 
	Recursively split and merge subsequences until the sequence 
		is sorted in ascencing order. 

	Discussion:
		Stable

	Time Complexity:
		Theta(n log(n))
	Space Complexity:
		O(n) auxiliary 
	Args:
		sequence:
			a list of comparable items
	Returns:
		list sorted in ascending order
	"""
	if len(sequence) <= 1:
		return sequence

	middle_index = len(sequence) // 2
	left_half = mergesort(sequence[:middle_index])
	right_half = mergesort(sequence[middle_index:])

	return merge(left_half, right_half)

def merge(left_half, right_half):
	""" Return a combined list of sorted elements from the two input lists. """
	
	combined_list = []
	left_index = 0
	right_index = 0

	while left_index < len(left_half) and right_index < len(right_half):
		if left_half[left_index] < right_half[right_index]:
			combined_list.append(left_half[left_index])
			left_index += 1
		else:
			combined_list.append(right_half[right_index])
			right_index += 1

	combined_list.extend(left_half[left_index:])
	combined_list.extend(right_half[right_index:])

	return combined_list
