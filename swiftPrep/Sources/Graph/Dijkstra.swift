
import Tree

func dijkstra(neighbors: [String: [String: Int]], source: String) 
	-> (visited: [String: Int], paths: [String: [String]]) {
	
	var visited = [source: 0]
	var paths = [source: [source]]
	var priorityQ = Heap<(Int, String)>(sequence: [(0, source)], orderedBy: <)

	while let (distance, vertex) = priorityQ.pop() {

		for (neighbor, edgeWeight) in neighbors[vertex]! {
			let dist_from_source_to_neighbor = distance + edgeWeight

			if visited[neighbor] == nil || 
				dist_from_source_to_neighbor < visited[neighbor]! {

				visited[neighbor] = dist_from_source_to_neighbor
				paths[neighbor] = paths[vertex]! + [neighbor]
				priorityQ.push((dist_from_source_to_neighbor, neighbor))
			}
		}
	}

	return (visited, paths)
}