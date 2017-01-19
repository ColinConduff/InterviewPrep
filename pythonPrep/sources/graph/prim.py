import heapq
from sources.graph.graph import *

def prim(graph):
	""" 
	Yield the minimum edges in the graph using Prim's Algorithm. 

	Time: O(|E| log |V|) using binary heap (faster with fibonacci heap)
	"""
	neighbors = graph.neighbors
	initial_vertex = next(iter(neighbors))
	visited = set([initial_vertex])
	priority_q = []

	for neighbor, edge_weight in neighbors[initial_vertex].items():
		heapq.heappush(priority_q, (edge_weight, initial_vertex, neighbor))

	while len(priority_q) > 0:
		edge_weight, u, v = heapq.heappop(priority_q)

		if v not in visited:
			visited.add(v)

			for w, next_edge_weight in neighbors[v].items():
				if w not in visited:
					heapq.heappush(priority_q, (next_edge_weight, v, w))

			yield u, v, edge_weight

def minimum_spanning_tree(graph):
	""" Return a minimum spanning tree for the graph. """
	ug = Graph(GraphType.UNDIRECTED)

	for u, v, edge_weight in prim(graph):
		ug.insert_edge(u, v, edge_weight)

	return ug
