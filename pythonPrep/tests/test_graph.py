#!/usr/bin/env python3

import unittest
from sources.graph.graph import *

class GraphTestCase(unittest.TestCase):

	def test_graph(self):
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


if __name__ == '__main__':
    unittests.main()