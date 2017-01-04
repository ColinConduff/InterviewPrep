import XCTest
@testable import Searching

class SearchingTests: XCTestCase {

  override func setUp() {
    super.setUp()
  }

  func testBinaryRecursiveSearch() {
    let test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for (num_index, num) in test.enumerated() {
      let resultIndex = binaryRecursiveSearch(sequence: test, key: num)
      XCTAssertEqual(num_index, resultIndex)
    }

    let resultIndex = binaryRecursiveSearch(sequence: test, key: 11)
    XCTAssertEqual(nil, resultIndex)
  }

  func testBinaryIterativeSearch() {
    let test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for (num_index, num) in test.enumerated() {
      let resultIndex = binaryIterativeSearch(sequence: test, key: num)
      XCTAssertEqual(num_index, resultIndex)
    }

    let resultIndex = binaryIterativeSearch(sequence: test, key: 11)
    XCTAssertEqual(nil, resultIndex)
  }
}