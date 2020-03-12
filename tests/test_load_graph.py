"""Unit tests for loading Graph dataset."""

import geomstats.tests
from geomstats.learning.graph_data_preparation import Graph


class TestLoadDefaultGraph(geomstats.tests.TestCase):
    """Test for loading graph-structured data."""

    def setUp(self):
        """Declare the graph by default and the Karate club graph."""
        self.G1 = Graph()
        self.G2 = Graph(
            Graph_Matrix_Path=r'examples\data_example\graph_karate\Karate.txt',
            Labels_Path=r'examples\data_example'
            r'\graph_karate\Karate_Labels.txt')

    def test_graph_load(self):
        """Test the correct number of edges and nodes for each graph."""
        result = [len(self.G1.edges) + len(self.G1.labels),
                  len(self.G2.edges) + len(self.G2.labels)]
        expected = [20, 68]
        self.assertAllClose(result, expected)

    def test_random_walks(self):
        """Test that random walks have the right length."""

        paths1 = self.G1.random_walk()
        paths2 = self.G2.random_walk()

        result = [len(paths1), len(paths2)]
        expected = [len(self.G1.edges), len(self.G2.edges)]
        self.assertAllClose(result, expected)