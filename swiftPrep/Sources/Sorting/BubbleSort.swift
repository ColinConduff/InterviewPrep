
func bubbleSort(sequence: inout [Int]) {
	for _ in 0..<sequence.count {
		var swapCount = 0

		for n in 1..<sequence.count {
			if sequence[n-1] > sequence[n] {
				(sequence[n-1], sequence[n]) = (sequence[n], sequence[n-1])

				swapCount += 1
			}
		}

		if swapCount == 0 {
			break
		}
	}
}