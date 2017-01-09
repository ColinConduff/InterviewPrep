import XCTest
@testable import SelectionAlgorithms

class SelectionAlgorithmsTests: XCTestCase {

  override func setUp() {
    super.setUp()
  }

  func testQuickselect() {

    var test1Sequence = [Int]()
    let solution1 = select(sequence: &test1Sequence, k: 1)
    XCTAssertTrue(solution1 == nil)

    var test2Sequence = [1]
    let solution2 = select(sequence: &test2Sequence, k: 1)
    XCTAssertTrue(solution2 == 1)

    // Test without reusing partially sorted sequence
    for k in 1...10 {
      var sequence = [8, 10, 7, 1, 5, 2, 9, 6, 4, 3]
      let solution = select(sequence: &sequence, k: k)
      XCTAssertTrue(solution == k) // kth smallest element == k
    }

    // Test while using partially sorted sequence

    var sequence = [8, 10, 7, 1, 5, 2, 9, 6, 4, 3]

    for k in 1...10 {
      let solution = select(sequence: &sequence, k: k, checkSorted: true)
      XCTAssertTrue(solution == k) // kth smallest element == k
    }
  }
}