import XCTest
@testable import DynamicProgrammingAlgs

class DynammicProgrammingAlgsTests: XCTestCase {

  override func setUp() {
    super.setUp()
  }

  func testLongestCommonSubstring() {
    
    let solution1 = "This is "
    let result1 = longestCommonSubstring(string1: "This is a test", string2: "This is not a test")

    //print("\n\nresult: \(result1)\n\n")
    XCTAssertTrue(solution1 == result1)

    let solution2 = ""
    let result2 = longestCommonSubstring(string1: "", string2: "This is not a test")

    //print("\n\nresult: \(result2)\n\n")
    XCTAssertTrue(solution2 == result2)

    let solution3 = ""
    let result3 = longestCommonSubstring(string1: "test", string2: "")

    //print("\n\nresult: \(result3)\n\n")
    XCTAssertTrue(solution3 == result3)

    let solution4 = "test"
    let result4 = longestCommonSubstring(string1: "test", string2: "test")

    //print("\n\nresult: \(result4)\n\n")
    XCTAssertTrue(solution4 == result4)
  }
}