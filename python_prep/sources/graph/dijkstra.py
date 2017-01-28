import heapq

def dijkstra(graph, source):
	
	neighbors = graph.neighbors # deep copy
	paths = {source: [source]}
	visited = {source: 0}
	priority_q = [(0, source)]

	while len(priority_q) > 0:
		distance, vertex = heapq.heappop(priority_q)

		for neighbor, edge_weight in neighbors[vertex].items():
			dist_from_source_to_neighbor = distance + edge_weight

			if neighbor not in visited or \
				dist_from_source_to_neighbor < visited[neighbor]:

				visited[neighbor] = dist_from_source_to_neighbor
				paths[neighbor] = paths[vertex] + [neighbor]
				heapq.heappush(priority_q, (dist_from_source_to_neighbor, neighbor))

	return (visited, paths)

				
