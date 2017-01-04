

func dijkstra(neighbors: [String: [String: Int]], source: String) -> ([String: Int], [String: [String]]) {
	
	var visited = [source: 0]
	var paths = [source: [source]]
	var priority_q = Heap<(Int, String)>(array: [(0, source)], sort: <)

	while let (distance, vertex) = priority_q.remove() {

		for (neighbor, edgeWeight) in neighbors[vertex]! {
			let dist_from_source_to_neighbor = distance + edgeWeight

			if visited[neighbor] == nil || 
				dist_from_source_to_neighbor < visited[neighbor]! {

				visited[neighbor] = dist_from_source_to_neighbor
				paths[neighbor] = paths[vertex]! + [neighbor]
				priority_q.insert((dist_from_source_to_neighbor, neighbor))
			}
		}
	}

	return (visited, paths)
}