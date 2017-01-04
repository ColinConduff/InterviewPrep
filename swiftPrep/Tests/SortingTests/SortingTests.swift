import XCTest
@testable import Sorting

class SortingTests: XCTestCase {

  let sortedSequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  var sequence = [10, 5, 9, 4, 8, 3, 7, 2, 6, 1]

  override func setUp() {
    super.setUp()
  }

  func resetSequence() {
    sequence = [10, 5, 9, 4, 8, 3, 7, 2, 6, 1]
  }

  func testBubbleSort() {
    resetSequence()
    bubbleSort(sequence: &sequence)
    XCTAssertEqual(sequence, sortedSequence)
  }

  func testSelectionSort() {
    resetSequence()
    selectionSort(sequence: &sequence)
    XCTAssertEqual(sequence, sortedSequence)
  }

  func testInsertionSort() {
    resetSequence()
    insertionSort(sequence: &sequence)
    XCTAssertEqual(sequence, sortedSequence)
  }

  func testCountingSort() {
    resetSequence()
    countingSort(sequence: &sequence)
    XCTAssertEqual(sequence, sortedSequence)
  }

  func testQuickSort() {
    resetSequence()
    qSort(sequence: &sequence)
    XCTAssertEqual(sequence, sortedSequence)
  }

  func testMergeSort() {
    resetSequence()
    let sorted = mergeSort(sequence: sequence)
    XCTAssertEqual(sorted, sortedSequence)
  }
}