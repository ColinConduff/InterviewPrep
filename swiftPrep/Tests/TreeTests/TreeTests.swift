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

  func testIntHeap() {
    var solution = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    var heap = Heap<Int>(sequence: solution, orderedBy: <)

    while let item = heap.pop(), let expected = solution.popLast() {
        XCTAssertEqual(item, expected)
    }

    var sequenceToPush = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    for num in sequenceToPush {
        heap.push(num)
    }

    while let item = heap.pop(), let expected = sequenceToPush.popLast() {
        XCTAssertEqual(item, expected)
    }
  }

  func testPriorityQueue() {
    var solution = [
        (10, "A"), (9, "B"), (8, "C"), (7, "A"), (6, "B"), 
        (5, "C"), (4, "C"), (3, "B"), (2, "A"), (1, "A")
    ]

    var heap = Heap<(Int, String)>(sequence: solution, orderedBy: <)

    while let item = heap.pop(), let expected = solution.popLast() {
        XCTAssertEqual(item.0, expected.0)
        XCTAssertEqual(item.1, expected.1)
    }

    var sequenceToPush = [
        (10, "A"), (9, "B"), (8, "C"), (7, "A"), (6, "B"), 
        (5, "C"), (4, "C"), (3, "B"), (2, "A"), (1, "A")
    ]
    
    for item in sequenceToPush {
        heap.push(item)
    }

    while let item = heap.pop(), let expected = sequenceToPush.popLast() {
        XCTAssertEqual(item.0, expected.0)
        XCTAssertEqual(item.1, expected.1)
    }
  }
}