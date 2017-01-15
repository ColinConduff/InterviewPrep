
def insertion_sort(sequence):
	""" Sort the sequence in place. Time: Omega(n), O(n^2). Space: O(1) aux. """
	for advancing_index in range(len(sequence)):
		key = sequence[advancing_index]
		retreating_index = advancing_index - 1

		while retreating_index >= 0 and sequence[retreating_index] > key:
			sequence[retreating_index + 1] = sequence[retreating_index]
			retreating_index -= 1

		sequence[retreating_index + 1] = key
