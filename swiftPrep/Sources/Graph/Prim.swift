
func prim(neighbors: [String: [String: Int]]) -> [(String, String, Int)] {
	
	guard let (startingVertex, _) = neighbors.first else { return [(String, String, Int)]() }
	var visited = Set([startingVertex])
	var priority_q = Heap<(Int, String, String)>(sort: <)
	
	var edges = [(String, String, Int)]()

	for (neighbor, edgeWeight) in neighbors[startingVertex]! {
		priority_q.insert((edgeWeight, startingVertex, neighbor))
	}

	while let (edgeWeight, u, v) = priority_q.remove() {
		if !visited.contains(v) {
			visited.insert(v)

			for (w, nextEdgeWeight) in neighbors[v]! {
				if !visited.contains(w) {
					priority_q.insert((nextEdgeWeight, v, w))
				}
			}

			edges.append((u, v, edgeWeight))
		}
	}

	return edges
}

func minimumSpanningTree(neighbors: [String: [String: Int]]) -> Graph {
	let g = Graph(type: .undirected)

	for (u, v, edgeWeight) in prim(neighbors: neighbors) {
		g.addEdge(from: u, to: v, edgeWeight: edgeWeight)
	}

	return g
}