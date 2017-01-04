
// With queue
// can replace string identifiers with AnyHashable type

func bfs(neighbors: [String: [String: Int]], 
		 source: String) -> [String: [String]] {

	guard neighbors[source] != nil else { return [String: [String]]() }

	var queue = ArraySlice(["A"])
	var visited = [source: [source]]

	while let vertex = queue.popFirst() {

		for (neighbor, _) in neighbors[vertex]! {
			if visited[neighbor] == nil {
				visited[neighbor] = visited[vertex]! + [neighbor]
				queue.append(neighbor)
			}
		}
	}

	return visited
}

/*
// without using a queue

func bfs(neighbors: [String: [String: Int]], 
		 source: String) -> [String: [String]] {

	guard neighbors[source] != nil else { return [String: [String]]() }

	var currentLevel = [source]
	var paths = [source: [source]]

	while currentLevel.count > 0 {
		var nextLevel = [String]()

		for vertex in currentLevel {
			for (neighbor, _) in neighbors[vertex]! {
				if paths[neighbor] == nil {
					paths[neighbor] = paths[vertex]! + [neighbor]
					nextLevel.append(neighbor)
				}
			}
		}

		currentLevel = nextLevel
	}

	return paths
}
*/