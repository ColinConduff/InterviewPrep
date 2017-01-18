#!/usr/bin/env python3

import unittest
from sources.graph.graph import *

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
		for component in components:
			self.assertTrue(component in [comp1, comp2])

		components = dg.connected_components()
		for component in components:
			self.assertTrue(component in [comp1, comp2])


if __name__ == '__main__':
    unittests.main()