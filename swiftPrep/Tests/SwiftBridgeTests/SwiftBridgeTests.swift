import XCTest
@testable import SwiftBridge

class SwiftBridgeTests: XCTestCase {

  override func setUp() {
    super.setUp()
  }

  func testCArrayList() {

    let array = CArrayList()

    for num in 1...20 {
      array.append(num)
    }

    XCTAssertTrue(array.count == 20)

    for _ in 1...20 {
      let _ = array.pop()
    }

    XCTAssertTrue(array.count == 0)

    array.insert(1, atIndex: 0)

    XCTAssertTrue(array.count == 1)
  }
}