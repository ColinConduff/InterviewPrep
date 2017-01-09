
import Darwin // for arc4random_uniform

/**
Select the kth smallest element from the sequence.

Time Complexity: O(n)
Space Complexity: O(log n)

Side-effect: Partially sorts the sequence.

If select is called multiple times, the sequence may eventually become sorted.
Can reduce the overall time complexity of successive calls by using the checkSorted parameter.  
*/
func select(sequence: inout [Int], k: Int, checkSorted: Bool=false) -> Int? {

	guard sequence.count > 0 else { return nil }
	guard k <= sequence.count && k > 0 else { return nil }
	guard sequence.count > 1 else { return sequence[k-1] }

	// O(n) if checkSorted = true
	if checkSorted && isSorted(sequence) {
		return sequence[k-1]
	}

	// O(n)
	return quickselect(sequence: &sequence, 
					   leftIndex: 0, 
					   rightIndex: sequence.endIndex-1, 
					   kIndex: k-1)
}

func isSorted(_ sequence: [Int]) -> Bool {
	for numIndex in 1..<sequence.endIndex {
		if sequence[numIndex-1] > sequence[numIndex] {
			return false
		}
	}
	return true
}

func quickselect(sequence: inout [Int], 
				 leftIndex: Int, 
				 rightIndex: Int, 
				 kIndex: Int) -> Int { 
	
	guard leftIndex != rightIndex else { return sequence[leftIndex] }

	let pivotIndex = Int(arc4random_uniform(UInt32(rightIndex - leftIndex))) + leftIndex
	let newPivotIndex = partition(sequence: &sequence, 
								  leftIndex: leftIndex, 
								  rightIndex: rightIndex, 
								  pivotIndex: pivotIndex)

	if kIndex < newPivotIndex {
		return quickselect(sequence: &sequence, leftIndex: leftIndex, rightIndex: newPivotIndex-1, kIndex: kIndex)
	
	} else if kIndex > newPivotIndex {
		return quickselect(sequence: &sequence, leftIndex: newPivotIndex+1, rightIndex: rightIndex, kIndex: kIndex)
	
	} else {
		return sequence[newPivotIndex]
	}
}

func partition(sequence: inout [Int], leftIndex: Int, rightIndex: Int, pivotIndex: Int) -> Int {
	
	let pivotValue = sequence[pivotIndex]
	(sequence[pivotIndex], sequence[rightIndex]) = (sequence[rightIndex], sequence[pivotIndex])
	var newPivotIndex = leftIndex

	for currentIndex in leftIndex..<rightIndex {
		if sequence[currentIndex] < pivotValue {
			(sequence[newPivotIndex], sequence[currentIndex]) = (sequence[currentIndex], sequence[newPivotIndex])
			newPivotIndex += 1
		}
	}

	(sequence[newPivotIndex], sequence[rightIndex]) = (sequence[rightIndex], sequence[newPivotIndex])

	return newPivotIndex
}