func insertionSort(sequence: inout [Int]) {
	for advancingIndex in 1..<sequence.count {
		let key = sequence[advancingIndex]
		var retreatingIndex = advancingIndex - 1

		while retreatingIndex >= 0 && sequence[retreatingIndex] > key {
			sequence[retreatingIndex + 1] = sequence[retreatingIndex]
			retreatingIndex -= 1
		}

		sequence[retreatingIndex + 1] = key
	}
}