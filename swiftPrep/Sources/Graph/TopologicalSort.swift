
func initialVertices(graph: Graph) -> Set<String> {

	// Find the vertices with in-degree = 0
	// slow, time: O(|E|)

	var vertices = Set(graph.neighbors.keys)
	
	for edges in graph.neighbors.values {
		for (neighbor, _) in edges {
			vertices.remove(neighbor)
		}
	}

	return vertices
}

func dfs(graph: Graph, visited: inout Set<String>, dfsOrder: inout [String], currentVertex: String) {

	// time: O(|E|)
	
	for (neighbor, _) in graph.neighbors[currentVertex]! {
		if !visited.contains(neighbor) {
			visited.insert(neighbor)
			dfsOrder.append(neighbor)
			dfs(graph: graph, visited: &visited, dfsOrder: &dfsOrder, currentVertex: neighbor)
		}
	}
}

func topologicalSort(graph: Graph) -> [String]? {
	
	// graph must be a DAG
	guard graph.graphType == .directed else { return nil }

	let startVertices = initialVertices(graph: graph)

	// unnecessary, no edges going to initial vertices
	var visited = Set(startVertices) 
	var dfsOrder = [String]()

	for vertex in startVertices {
		dfsOrder.append(vertex)
		dfs(graph: graph, visited: &visited, dfsOrder: &dfsOrder, currentVertex: vertex)
	}

	dfsOrder.reverse()

	return dfsOrder
}