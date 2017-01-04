
func mergeSort(sequence: [Int]) -> [Int] {
	guard sequence.count > 1 else { return sequence }

	let middleIndex = sequence.count / 2 

	let leftSlice = Array(sequence.prefix(middleIndex))
	let rightSlice = Array(sequence.suffix(from: middleIndex))

	let leftHalf = mergeSort(sequence: leftSlice)
	let rightHalf = mergeSort(sequence: rightSlice)

	return merge(leftHalf: leftHalf, rightHalf: rightHalf)
}

func merge(leftHalf: [Int], rightHalf: [Int]) -> [Int] {

	var combinedList = [Int]()
	var leftIndex = leftHalf.startIndex
	var rightIndex = rightHalf.startIndex

	while leftIndex < leftHalf.endIndex && rightIndex < rightHalf.endIndex {
		if leftHalf[leftIndex] < rightHalf[rightIndex] {
			combinedList.append(leftHalf[leftIndex])
			leftIndex += 1
		} else {
			combinedList.append(rightHalf[rightIndex])
			rightIndex += 1
		}
	}

	combinedList.append(contentsOf: leftHalf.suffix(from: leftIndex))
	combinedList.append(contentsOf: rightHalf.suffix(from: rightIndex))

	return combinedList
}