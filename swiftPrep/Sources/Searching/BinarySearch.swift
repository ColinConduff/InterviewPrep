
func _recursiveSearch(sequence: [Int], key: Int, leftIndex: Int, rightIndex: Int) -> Int? {
	
	guard leftIndex <= rightIndex else { return nil }

	let middleIndex = leftIndex + (rightIndex - leftIndex) / 2

	if key < sequence[middleIndex] {
		return _recursiveSearch(sequence: sequence, key: key, leftIndex: leftIndex, rightIndex: middleIndex - 1)
	} else if key > sequence[middleIndex] {
		return _recursiveSearch(sequence: sequence, key: key, leftIndex: middleIndex + 1, rightIndex: rightIndex)
	} else {
		return middleIndex
	}
}

func binaryRecursiveSearch(sequence: [Int], key: Int) -> Int? {
	
	return _recursiveSearch(sequence: sequence, key: key, leftIndex: 0, rightIndex: sequence.count - 1)

}

func binaryIterativeSearch(sequence: [Int], key: Int) -> Int? {
	
	var leftIndex = 0
	var rightIndex = sequence.count - 1

	while leftIndex <= rightIndex {
		let middleIndex = leftIndex + (rightIndex - leftIndex) / 2

		if key < sequence[middleIndex] {
			rightIndex = middleIndex - 1
		} else if key > sequence[middleIndex] {
			leftIndex = middleIndex + 1
		} else {
			return middleIndex
		}
	}

	return nil
}