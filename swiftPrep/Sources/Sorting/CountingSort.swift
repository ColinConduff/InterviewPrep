func countingSort(sequence: inout [Int]) {
	guard sequence.count > 1 else { return }

	let minNumber = sequence.min()!
	let maxNumber = sequence.max()! + 1

	var frequencies = Array<Int>(repeating: 0, count: maxNumber - minNumber)

	for number in sequence {
		frequencies[number - minNumber] += 1
	}

	var index = 0

	for number in minNumber..<maxNumber {
		let frequency = frequencies[number - minNumber]

		for _ in 0..<frequency {
			sequence[index] = number
			index += 1
		}
	}
}