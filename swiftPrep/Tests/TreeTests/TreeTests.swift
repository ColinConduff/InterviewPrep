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
}