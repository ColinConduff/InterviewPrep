
enum GraphType {
	case undirected, directed
}

class Graph {
	
	var neighbors = [String: [String: Int]]()
	var graphType: GraphType

	required init(type: GraphType, edges: [String: [String: Int]]) {
		self.graphType = type

		for (vertex, values) in edges {
			for (neighbor, weight) in values {
				self.addEdge(from: vertex, to: neighbor, edgeWeight: weight)
			}
		}
	}

	required init(type: GraphType) {
		self.graphType = type
	}

	func add(vertex: String) {
		if self.neighbors[vertex] == nil {
			self.neighbors[vertex] = [String: Int]() // unnecessary?
		}
	}

	func addEdge(from source: String, 
				  to destination: String, 
				  edgeWeight: Int = 0) {

		self.add(vertex: source)
		self.add(vertex: destination)

		if self.neighbors[source]![destination] == nil {
			self.neighbors[source]![destination] = edgeWeight
		}

		if graphType == .undirected {
			if self.neighbors[destination]![source] == nil {
				self.neighbors[destination]![source] = edgeWeight
			}
		}
	}

	var description: String {
		get {
			var result = ""
			
			for (source, value) in self.neighbors {
				//let (destination, weight) = value

				result += "\(source) -> \(value)\n"
			}

			return result
		}
	}

	static func == (lhs: Graph, rhs: Graph) -> Bool {
		for (vertex, lhsEdge) in lhs.neighbors {
			guard let rhsEdge = rhs.neighbors[vertex],
				lhsEdge == rhsEdge
			else {
				return false
			}
		}

		return true
	}
}

