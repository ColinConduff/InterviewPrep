
func fibNum(n: Int, precomputed: inout [Int]) -> Int? {
	// fib sequence: 0, 1, 1, 2, 3, 5, 8 ...
	
	// precomputed sequence allows caller to store computed values
	// for later use

	guard n > 0 else { return nil }

	if precomputed.count < 2 {
		precomputed = [0, 1]
	}

	if precomputed.endIndex <= n {
		for index in precomputed.endIndex...n {
			precomputed.append(precomputed[index-2] + precomputed[index-1])
		}
	}

	return precomputed[n-1]
}