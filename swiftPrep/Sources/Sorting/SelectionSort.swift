func selectionSort(sequence: inout [Int]) {
	for outerIndex in 0..<sequence.count {
		var minIndex = outerIndex

		for innerIndex in outerIndex+1..<sequence.count {
			if sequence[innerIndex] < sequence[minIndex] {
				minIndex = innerIndex
			}
		}

		(sequence[outerIndex], sequence[minIndex]) = (sequence[minIndex], sequence[outerIndex])
	}
}