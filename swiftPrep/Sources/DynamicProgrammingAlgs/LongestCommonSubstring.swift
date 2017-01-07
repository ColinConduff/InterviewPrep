
func longestCommonSubstring(string1: String, string2: String) -> String {
	
	// Overall complexity
	// Time: O(|string1| * |string2|)
	// Space: O(|string1| * |string2|)

	let numRows = string1.characters.count + 1
	let numCols = string2.characters.count + 1

	// Space: O(|string1| |string2|)
	var matrix = Array(repeating: Array(repeating: 0, count: numCols), count: numRows)

	// Strings are a pain to work with
	let char1Array = Array(string1.characters) // Space: O(|string1|)
	let char2Array = Array(string2.characters) // Space: O(|string2|)

	var longestSubstring = [Character]() // Space: O(|longestCommonSubstring|)
	var longestSubstringLength = 0

	// Time: O(|string1| |string2|)
	for rowIndex in 1..<numRows {
		for colIndex in 1..<numCols {

			let char1 = char1Array[rowIndex - 1]
			let char2 = char2Array[colIndex - 1]

			if char1 == char2 {
				let prevSubstringLength = matrix[rowIndex-1][colIndex-1]
				let currentSubstringLength = prevSubstringLength + 1
				matrix[rowIndex][colIndex] = currentSubstringLength

				if currentSubstringLength > longestSubstringLength {
					longestSubstringLength = currentSubstringLength

					// Time Complexity ??? Amortized O(1)
					longestSubstring = Array(char1Array.prefix(upTo: rowIndex).suffix(from: rowIndex - longestSubstringLength))
				
				} else if currentSubstringLength == longestSubstringLength {
					longestSubstring.append(char1)
				}
			}
		}
	}

	return String(longestSubstring)
}