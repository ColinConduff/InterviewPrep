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

