
func _dfs(neighbors: [String: [String: Int]], visited: inout [String: [String]], vertex: String) {

	for (neighbor, _) in neighbors[vertex]! {
		if visited[neighbor] == nil {
			visited[neighbor] = visited[vertex]! + [neighbor]
			_dfs(neighbors: neighbors, visited: &visited, vertex: neighbor)
		}
	}

}

func dfs(neighbors: [String: [String: Int]], source: String) -> [String: [String]] {

    var visited = [source: [source]]

    _dfs(neighbors: neighbors, visited: &visited, vertex: source)

    return visited
}

func dfs_iterative(neighbors: [String: [String: Int]], source: String) -> [String: [String]] 
{
	var visited = [source: [source]]
	var stack = [source]

	while let vertex = stack.pop() {
		for (neighbor, _) in neighbors[vertex]! {
			if visited[neighbor] == nil {
				visited[neighbor] = visited[vertex]! + [neighbor]
				stack.append(neighbor)
			}
		}
	}

	return visited
}