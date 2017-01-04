import Darwin

func qSort(sequence: inout [Int]) {
	quickSort(sequence: &sequence, leftIndex: 0, rightIndex: sequence.count - 1)
}

func quickSort(sequence: inout [Int], leftIndex: Int, rightIndex: Int) {
	guard sequence.count > 1 && leftIndex < rightIndex else { return }
	
	let pivotIndex = Int(arc4random_uniform(UInt32(rightIndex - leftIndex))) + leftIndex
	let newPivotIndex = partition(&sequence, leftIndex, rightIndex, pivotIndex)

	quickSort(sequence: &sequence, leftIndex: leftIndex, rightIndex: newPivotIndex - 1)
	quickSort(sequence: &sequence, leftIndex: newPivotIndex + 1, rightIndex: rightIndex)
}

func partition(_ sequence: inout [Int], _ leftIndex: Int, _ rightIndex: Int, _ pivotIndex: Int) -> Int {
	let pivotValue = sequence[pivotIndex]
	var newPivotIndex = leftIndex
	(sequence[pivotIndex], sequence[rightIndex]) = (sequence[rightIndex], sequence[pivotIndex])

	for currentIndex in leftIndex..<rightIndex {
		if sequence[currentIndex] < pivotValue {
			(sequence[currentIndex], sequence[newPivotIndex]) = (sequence[newPivotIndex], sequence[currentIndex])
			newPivotIndex += 1
		}
	}

	(sequence[rightIndex], sequence[newPivotIndex]) = (sequence[newPivotIndex], sequence[rightIndex])

	return newPivotIndex
}