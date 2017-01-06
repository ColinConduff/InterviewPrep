
fileprivate class Node {
	var data = [Character: Node]()
	init() { }
}

struct Trie {

	private var root = Node()
	
	init() { }

	mutating func add(word: String) {
		var currentNode = root

		for letter in word.characters {

			if currentNode.data[letter] == nil {
				currentNode.data[letter] = Node()
			}
			
			currentNode = currentNode.data[letter]!
		}

		// denotes end of word
		currentNode.data["\n"] = Node() // replace with nil?
	}

	func contains(word: String) -> Bool {
		var currentNode = root

		for letter in word.characters {
			if currentNode.data[letter] == nil {
				return false
			}
			
			currentNode = currentNode.data[letter]!
		}

		return currentNode.data["\n"] != nil
	}

	private func _findWords(currentNode: Node, currentWord: String, words: Set<String>) -> Set<String> {

		// using sets to prevent duplicates or passing by reference

		var words = words

		for (letter, nextNode) in currentNode.data {

			if letter == "\n" {
				words.insert(currentWord)

			} else {
				let nextWord = currentWord + String(letter)

				words = words.union(_findWords(currentNode: nextNode, currentWord: nextWord, words: words))
			}
		}

		return words
	}

	func wordsStartingWith(prefix: String) -> [String] {

		var currentNode = root

		for letter in prefix.characters {

			if let nextNode = currentNode.data[letter] {
				currentNode = nextNode
			} else {
				return [String]()
			}			
		}

		let wordSet = _findWords(currentNode: currentNode, currentWord: prefix, words: Set<String>())

		return Array(wordSet)
	}
}