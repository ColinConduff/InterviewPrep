import XCTest
@testable import Graph

class GraphTests: XCTestCase {

  let undirectedEdges = [
    "A": ["B": 3, "C": 2], 
    "B": ["A": 3], 
    "C": ["A": 2]
  ]

  let directedEdges = [
    "A": ["B": 3, "C": 2], 
    "B": [:], 
    "C": [:]
  ]

  override func setUp() {
    super.setUp()
  }

  func testGraphComparison() {

    let g1 = Graph(type: .undirected, edges: undirectedEdges)
    let g2 = Graph(type: .undirected, edges: undirectedEdges)
    let g3 = Graph(type: .directed, edges: directedEdges)

    XCTAssertTrue(g1 == g2)
    XCTAssertFalse(g1 == g3)
  }

  func testUndirectedGraph() {

    let g = Graph(type: .undirected, edges: undirectedEdges)

    for (vertex, _) in undirectedEdges {
      XCTAssertEqual(undirectedEdges[vertex]!, g.neighbors[vertex]!)
    }
  }

  func testDirectedGraph() {

    let g = Graph(type: .directed, edges: directedEdges)

    for (vertex, _) in directedEdges {
      XCTAssertEqual(directedEdges[vertex]!, g.neighbors[vertex]!)
    }
  }

  func testBFS() {

    let g = Graph(type: .undirected, edges: undirectedEdges)
    let expectedPaths = ["A": ["A"], "B": ["A", "B"], "C": ["A", "C"]]
    let paths = bfs(neighbors: g.neighbors, source: "A")

    for (vertex, _) in expectedPaths {
      XCTAssertEqual(expectedPaths[vertex]!, paths[vertex]!)
    }
  }

  func testDFS() {

    let g = Graph(type: .undirected, edges: undirectedEdges)
    let expectedPaths = ["A": ["A"], "B": ["A", "B"], "C": ["A", "C"]]
    let paths = dfs(neighbors: g.neighbors, source: "A")

    for (vertex, _) in expectedPaths {
      XCTAssertEqual(expectedPaths[vertex]!, paths[vertex]!)
    }
  }

  func testDijkstra() {
    let dijkstraEdges = [
      "S": ["U": 10, "X": 5],
      "U": ["V": 1],
      "V": ["Y": 4],
      "X": ["U": 3, "V": 9, "Y": 2],
      "Y": ["S": 7]
    ]

    let g = Graph(type: .directed, edges: dijkstraEdges)

    let (distances, _) = dijkstra(neighbors: g.neighbors, source: "S")

    let solutionDistances = [
      "U": 8, "Y": 7, "X": 5, "S": 0, "V": 9
    ]

    XCTAssertEqual(distances, solutionDistances)
  }

  func testPrim() {
    let primEdges = [
      "A": ["B": 1, "D": 4, "E": 3],
      "B": ["D": 4, "E": 2],
      "C": ["E": 4, "F": 5],
      "D": ["E": 4],
      "E": ["F": 7]
    ]
    let g = Graph(type: .undirected, edges: primEdges)

    let mst = minimumSpanningTree(neighbors: g.neighbors)

    let solutionEdges = [
      "A": ["B": 1, "D": 4],
      "B": ["E": 2],
      "C": ["E": 4, "F": 5]
    ]

    let solution = Graph(type: .undirected, edges: solutionEdges)

    XCTAssertTrue(mst == solution)
  }

  func testTopoSort() {
    let dagEdges = [
      "G": ["H": 0],
      "A": ["H": 0, "B": 0],
      "B": ["C": 0],
      "C": ["F": 0],
      "D": ["C": 0, "E": 0],
      "E": ["F": 0],
      "I": [:]
    ]

    // topo sorts are not unique/ multiple solutions possible
    let solution = ["I", "G", "E", "D", "F", "C", "B", "H", "A"]

    let g = Graph(type: .directed, edges: dagEdges)

    let topoSort = topologicalSort(graph: g)!

    XCTAssertTrue(topoSort == solution)
  }
}