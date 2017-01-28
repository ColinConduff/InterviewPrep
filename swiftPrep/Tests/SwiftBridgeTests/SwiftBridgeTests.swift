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

  func testCCircularBuffer() {
    
    let ccb = CCircularBuffer()
    let test1 = Array(1...16)
    
    for num in test1 {
      ccb.enqueue(num)
    }
    
    XCTAssertTrue(ccb.count == 16)
    
    for num in test1 {
      XCTAssertTrue(num == ccb.dequeue())
    }
    
    XCTAssertTrue(ccb.count == 0)

    let test2 = Array(1...8)
    
    for num in test2 {
      ccb.enqueue(num)
    }

    XCTAssertTrue(ccb.count == 8)

    XCTAssertTrue(1 == ccb.dequeue())
    XCTAssertTrue(2 == ccb.dequeue())

    XCTAssertTrue(ccb.count == 6)
  }
}