import XCTest
@testable import LinkedLists

class LinkedListsTests: XCTestCase {

  override func setUp() {
    super.setUp()
  }

  func testCircularlyLinkedLists() {

    var cll = CircularlyLinkedList()

    cll.appendFront(data: 2)
    cll.appendFront(data: 1)

    XCTAssertTrue(cll == [1, 2])
    XCTAssertEqual(cll.count, 2)

    cll.appendBack(data: 3)
    cll.appendBack(data: 4) 

    XCTAssertTrue(cll == [1, 2, 3, 4])
    XCTAssertEqual(cll.count, 4)

    XCTAssertEqual(cll.popFront(), 1)
    XCTAssertEqual(cll.popFront(), 2)

    XCTAssertTrue(cll == [3, 4])
    XCTAssertEqual(cll.count, 2)

    XCTAssertEqual(cll.popBack(), 4)
    XCTAssertEqual(cll.popBack(), 3)

    XCTAssertTrue(cll == [])
    XCTAssertEqual(cll.count, 0)

    cll.appendBack(data: 1)

    XCTAssertTrue(cll == [1])
    XCTAssertEqual(cll.count, 1)

    cll.clear()
    XCTAssertEqual(cll.count, 0)
    XCTAssertEqual(cll.popFront(), nil)
    XCTAssertEqual(cll.count, 0)
    XCTAssertEqual(cll.popBack(), nil)
    XCTAssertEqual(cll.count, 0)
  }
}