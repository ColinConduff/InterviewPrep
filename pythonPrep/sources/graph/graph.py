from enum import Enum
from copy import deepcopy

class GraphType(Enum):
	DIRECTED = "Directed Graph"
	UNDIRECTED = "Undirected Graph"

	def __str__(self):
		return '{}'.format(self.value)


class Graph(object):
	
	def __init__(self, type=GraphType.DIRECTED):
		self._graph_type = type
		self._neighbors = {}
		self._vertex_count = 0
		self._edge_count = 0

	@property
	def vertex_count(self):
		return self._vertex_count

	@property
	def edge_count(self):
		return self._edge_count

	@property
	def graph_type(self):
		return str(self._graph_type)

	@property 
	def neighbors(self):
		""" Allow read-only access to neighbors. """
		return deepcopy(self._neighbors)

	def __getitem__(self, vertex):
		""" Return dictionary containing edges connected to vertex. """
		return deepcopy(self._neighbors[vertex])

	def __contains__(self, vertex):
		return vertex in self._neighbors

	def __iter__(self):
		return iter(self._neighbors)

	def insert_vertex(self, vertex):
		if vertex not in self._neighbors:
			self._neighbors[vertex] = {}
			self._vertex_count += 1

	def insert_edge(self, source, destination, edge_weight=1):
		self.insert_vertex(source)
		self.insert_vertex(destination)

		if destination not in self._neighbors[source]:
			self._neighbors[source][destination] = edge_weight
			self._edge_count += 1

		if self._graph_type == GraphType.UNDIRECTED:
			if source not in self._neighbors[destination]:
				self._neighbors[destination][source] = edge_weight

	def remove_edge(self, source, destination):
		if destination in self._neighbors[source]:
			del self._neighbors[source][destination]
			self._edge_count -= 1

		if self._graph_type == GraphType.UNDIRECTED:
			if source in self._neighbors[destination]:
				del self._neighbors[destination][source]

	def remove_vertex(self, vertex):
		if vertex in self._neighbors:
			for neighbor in list(self._neighbors[vertex]):
				self.remove_edge(vertex, neighbor)
			
			del self._neighbors[vertex]
			self._vertex_count -= 1

	def cycle_found(self, source):
		""" 
		Use iterative DFS to detect cycles. 
		Time: O(|V| + |E|)
		Space: O(|V|)
		"""
		stack = [source]
		visited = set([source])
		
		while len(stack) > 0:
			vertex = stack.pop()

			for neighbor in self._neighbors[vertex]:
				if neighbor in visited:
					return True

				visited.add(neighbor)
				stack.append(neighbor)

		return False

	def connected_components(self):
		"""
		Return the graph's connected components.

		Time: O(|V| + |E|) 
		Space: O(|V|)

		Returns:
			list of components (sets of vertices)
		"""

		components = []

		if self._graph_type == GraphType.DIRECTED:
			# Consider using a union-find / disjoint-set instead
			unvisited = self.vertices_with_in_degree_0()
		else:
			unvisited = set(self._neighbors)
		
		while len(unvisited) > 0:
			initial_vertex = next(iter(unvisited))

			unvisited.remove(initial_vertex)
			stack = [initial_vertex]
			component = set(initial_vertex)

			# Iterative DFS
			while len(stack) > 0:
				vertex = stack.pop()
				
				for neighbor in self._neighbors[vertex]:
					if neighbor not in component:
						stack.append(neighbor)
						component.add(neighbor)

						if neighbor in unvisited:
							unvisited.remove(neighbor)
			
			components.append(component)

		return components

	def vertices_with_in_degree_0(self):
		""" O(|V| + |E|) """
		in_degree_0 = set(self._neighbors)

		for vertex in self._neighbors:
			for neighbor in self._neighbors[vertex]:
				if neighbor in in_degree_0:
					in_degree_0.remove(neighbor)

		return in_degree_0



