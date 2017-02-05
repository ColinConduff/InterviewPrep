
import Tree

func prim(neighbors: [String: [String: Int]]) -> [(String, String, Int)] {
	
	guard let (startingVertex, _) = neighbors.first else { return [(String, String, Int)]() }
	var visited = Set([startingVertex])
	var priorityQ = Heap<(Int, String, String)>(orderedBy: <)
	
	var edges = [(String, String, Int)]()

	for (neighbor, edgeWeight) in neighbors[startingVertex]! {
		priorityQ.push((edgeWeight, startingVertex, neighbor))
	}

	while let (edgeWeight, u, v) = priorityQ.pop() {
		if !visited.contains(v) {
			visited.insert(v)

			for (w, nextEdgeWeight) in neighbors[v]! {
				if !visited.contains(w) {
					priorityQ.push((nextEdgeWeight, v, w))
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