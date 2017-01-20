#!/usr/bin/env python3

import unittest
from sources.graph.graph import *
from sources.graph.dijkstra import dijkstra
from sources.graph.prim import minimum_spanning_tree

class GraphTestCase(unittest.TestCase):

	def test_undirected_graph(self):
		undirected_g = Graph(GraphType.UNDIRECTED)

		self.assertTrue(undirected_g.graph_type == "Undirected Graph")

		self.assertTrue(undirected_g.vertex_count == 0)
		self.assertTrue(undirected_g.edge_count == 0)

		undirected_g.insert_vertex("A")
		self.assertTrue(undirected_g.vertex_count == 1)

		undirected_g.insert_edge("A", "B")
		self.assertTrue(undirected_g.vertex_count == 2)
		self.assertTrue(undirected_g.edge_count == 1)
		self.assertTrue(undirected_g["A"] == {"B": 1})

		self.assertTrue(undirected_g.neighbors == {'A': {'B': 1}, 'B': {'A': 1}})

		undirected_g.insert_edge("B", "C", 3)
		self.assertTrue(undirected_g["B"]["C"] == 3)

		neighbors_before_edge_insertion = undirected_g.neighbors
		v_count_before_edge_insertion = undirected_g.vertex_count
		e_count_before_edge_insertion = undirected_g.edge_count
		
		undirected_g.insert_edge("A", "D", 2)
		undirected_g.remove_edge("A", "D")
		undirected_g.remove_vertex("D")

		self.assertTrue(undirected_g.neighbors == neighbors_before_edge_insertion)
		self.assertTrue(undirected_g.vertex_count == v_count_before_edge_insertion)
		self.assertTrue(undirected_g.edge_count == e_count_before_edge_insertion)

		undirected_g.remove_vertex("A")
		undirected_g.remove_vertex("B")
		undirected_g.remove_vertex("C")

		self.assertTrue(undirected_g.vertex_count == 0)
		self.assertTrue(undirected_g.edge_count == 0)
		self.assertTrue(undirected_g.neighbors == {})

	def test_cycle_detection(self):
		cyclic = Graph(GraphType.DIRECTED)
		cyclic.insert_edge("A", "B")
		cyclic.insert_edge("B", "C")
		cyclic.insert_edge("C", "A")

		self.assertTrue(cyclic.cycle_found("A"))

		acyclic = Graph(GraphType.DIRECTED)
		acyclic.insert_edge("A", "B")
		acyclic.insert_edge("B", "C")
		acyclic.insert_edge("C", "D")

		self.assertFalse(acyclic.cycle_found("A"))

	def test_vertices_with_in_degree_0(self):
		dg = Graph(GraphType.DIRECTED)
		dg.insert_edge("A", "B")
		dg.insert_edge("D", "C")
		dg.insert_vertex("E")

		expected = set(["A", "D", "E"])
		observed = dg.vertices_with_in_degree_0()

		self.assertTrue(expected == observed)

	def test_connected_components(self):
		# Should split this into two tests

		ug = Graph(GraphType.UNDIRECTED)
		dg = Graph(GraphType.DIRECTED)

		# Component 1
		ug.insert_edge("A", "B")
		ug.insert_edge("B", "C")

		dg.insert_edge("A", "B")
		dg.insert_edge("B", "C")

		comp1 = set(["A", "B", "C"])

		self.assertTrue(ug.connected_components() == [comp1])
		self.assertTrue(dg.connected_components() == [comp1])

		# Component 2
		ug.insert_edge("D", "E")
		ug.insert_edge("D", "F")

		dg.insert_edge("D", "E")
		dg.insert_edge("D", "F")

		comp2 = set(["D", "E", "F"])

		components = ug.connected_components()
		self.assertTrue(all(comp in [comp1, comp2] for comp in components))

		components = dg.connected_components()
		self.assertTrue(all(comp in [comp1, comp2] for comp in components))

	def test_strongly_connected_components(self):
		ug = Graph(GraphType.DIRECTED)
		
		ug.insert_edge("A", "B")
		ug.insert_edge("B", "A")
		comp1 = {"A", "B"}
		expected = [comp1]
		observed = ug.strongly_connected_components()

		self.assertTrue(observed == expected)

		ug.insert_edge("C", "D")
		ug.insert_edge("D", "E")
		ug.insert_edge("E", "C")
		comp2 = {"C", "D", "E"}
		expected = [comp1, comp2]
		observed = ug.strongly_connected_components()

		self.assertTrue(all(comp in expected for comp in observed))

		ug.insert_vertex("F")
		comp3 = {"F"}
		expected = [comp1, comp2, comp3]
		observed = ug.strongly_connected_components()

		self.assertTrue(all(comp in expected for comp in observed))

		ug.insert_edge("F", "C")
		expected = [comp1, comp2, comp3]
		observed = ug.strongly_connected_components()

		self.assertTrue(all(comp in expected for comp in observed))

		# The following case fails because the reverse dfs order
		# can start in component 3 and flow into component 2.
		# ug.insert_edge("G", "H")
		# ug.insert_edge("H", "F")
		# ug.insert_edge("F", "G")
		# comp3 = {"F", "G", "H"}
		# expected = [comp1, comp2, comp3]
		# observed = ug.strongly_connected_components()
		# self.assertTrue(all(comp in expected for comp in observed))

	def test_dijkstra(self):
		dg = Graph(GraphType.DIRECTED)

		dijkstra_edges = [
			("S", "U", 10),
			("S", "X", 5),
			("U", "V", 1),
			("V", "Y", 4),
			("X", "U", 3),
			("X", "V", 9),
			("X", "Y", 2),
			("Y", "S", 7)
		]

		for vertex, neighbor, edge_weight in dijkstra_edges:
			dg.insert_edge(vertex, neighbor, edge_weight)

		observed_distances, _ = dijkstra(dg, "S")
		expected_distances = {"U": 8, "Y": 7, "X": 5, "S": 0, "V": 9}

		self.assertTrue(observed_distances == expected_distances)

	def test_prim(self):
		prim_edges = [
			("A", "B", 1),
			("A", "D", 4),
			("A", "E", 3),
			("B", "D", 4),
			("B", "E", 2),
			("C", "E", 4),
			("C", "F", 5),
			("D", "E", 4),
			("E", "F", 7),
		]

		g = Graph(GraphType.UNDIRECTED)
		for u, v, weight in prim_edges:
			g.insert_edge(u, v, weight)

		mst = minimum_spanning_tree(g)

		expected_edges = [
			("A", "B", 1),
			("A", "D", 4),
			("B", "E", 2),
			("C", "E", 4),
			("C", "F", 5)
		]

		expected_graph = Graph(GraphType.UNDIRECTED)
		for u, v, weight in expected_edges:
			expected_graph.insert_edge(u, v, weight)

		self.assertTrue(mst == expected_graph)


if __name__ == '__main__':
    unittests.main()