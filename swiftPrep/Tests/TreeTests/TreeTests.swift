import XCTest
@testable import Tree

class TreeTests: XCTestCase {

  override func setUp() {
    super.setUp()
  }

  func testBST() {

    var bst = BST()

    XCTAssertTrue(bst.size == 0)

    // Test put/insert
    bst[1] = 1
    bst[2] = 2
    bst[3] = 3
    bst[4] = 4
    XCTAssertTrue(bst.size == 4)

    // Test put/update
    bst[4] = 5
    XCTAssertTrue(bst[4] == 5)
    
    // Test delete
    bst[1] = nil
    XCTAssertTrue(bst.size == 3)
    
    // Test get and contains
    XCTAssertTrue(bst.contains(key: 2))
    XCTAssertFalse(bst.contains(key: 1))
  }

  func testTrie() {
    var trie = Trie()

    let words = ["This", "This is", "This is a test"]

    for word in words {
        trie.add(word: word)
    }

    for word in words {
        XCTAssertTrue(trie.contains(word: word))
    }

    XCTAssertFalse(trie.contains(word: "False"))

    XCTAssertEqual(Set(words), Set(trie.wordsStartingWith(prefix: "")))
  }

  func testHeap() {
    var sequence = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    var solution = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    heapify(&sequence)

    while let item = heappop(&sequence), let expected = solution.popLast() {
        XCTAssertEqual(item, expected)
    }

    let sequenceToPush = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    let uniqueSolution = [1, 2, 6, 5, 3, 10, 7, 10, 8, 9, 4]
    
    for num in sequenceToPush {
        heappush(&sequence, item: num)
    }

    XCTAssertEqual(sequence, uniqueSolution)
  }
}