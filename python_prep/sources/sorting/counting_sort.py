def counting_sort(sequence):
	""" 
	Sort the sequence in ascending order. 

	Time: O(n+k) where k is the range 
	Space: O(n+k)
	"""
	if len(sequence) <= 1:
		return 

	min_num = min(sequence)
	max_num = max(sequence) + 1

	frequencies = [ 0 for _ in range(min_num, max_num) ]

	for num in sequence:
		frequencies[ num - min_num ] += 1
	
	# StopIteration error should not occur
	index = iter(range(len(sequence)))

	for num in range(min_num, max_num):
		frequency = frequencies[ num - min_num ]

		for _ in range(frequency):
			sequence[next(index)] = num
