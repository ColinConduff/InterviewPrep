
/**
	Sort the sequence in ascending order in place.

	Time: O(n^2), Omega(n)
	Space: O(1)

	A sequence can be sorted online by calling insertionSort
	multiple times while passing in the startIndex of newly added items.
	
	:param: sequence The sequence to sort in place.
	:param: startIndex The index to start sorting at.
 */
func insertionSort(sequence: inout [Int], startIndex: Int=1) {
	for advancingIndex in startIndex..<sequence.count {
		let key = sequence[advancingIndex]
		var retreatingIndex = advancingIndex - 1

		while retreatingIndex >= 0 && sequence[retreatingIndex] > key {
			sequence[retreatingIndex + 1] = sequence[retreatingIndex]
			retreatingIndex -= 1
		}

		sequence[retreatingIndex + 1] = key
	}
}