from scripts.graphs.Graph import Edge, Graph, Node, GraphAlgorithm
from scripts.Algorithm import AlgorithmError

from datetime import datetime
import networkx as nx


class DetectCycleAlgorithm(GraphAlgorithm):
    """
    Class of algorithms which detect if there is at least one cycle in the provided graph.
    """

    def has_worked(self):
        """
        Determines if the algorithm correctly detected cycles in the graph, as intended.
        :raise: AlgorithmError if a cycle was detected where there isn't one, or vice versa.
        :return: True if the algorithm detected the correct number of cycles.
        """

        g = nx.Graph()

        for edge in self.oldcollection.edges:
            g.add_edge(edge.source.label, edge.destination.label, weight=edge.distance)

        # list of cycles not stored in self.newcollection
        if len(list(nx.simple_cycles(g))) != len(self.output):
            raise AlgorithmError("Incorrect number of cycles detected.")

        return True

    def execute(self):
        """
        Executes the graph algorithm's steps on the provided graph.
        """

        raise NotImplementedError("Please use a specific graph algorithm's execute() function.")

    @staticmethod
    def metadata():
        """
        Returns the algorithm's metadata - space complexity, time complexity, algorithm description etc.
        """

        raise NotImplementedError("Please use a specific graph algorithm's metadata() function.")


class Kosaraju(DetectCycleAlgorithm):
    """
    Algorithm class for the Kosaraju algorithm - a DFS algorithm for detecting simple cycles in graphs.
    """

    description = """"""
    steps = []
    best_case = ""
    average_case = ""
    worst_case = ""

    @staticmethod
    def metadata():
        return {
            "description": Kosaraju.description,
            "steps": Kosaraju.steps,
            "best_case": Kosaraju.best_case,
            "worst_case": Kosaraju.worst_case,
            "average_case": Kosaraju.average_case
        }

    # TODO
    def execute(self):
        """
        Finds all the cycles in the provided graph using Kosaraju's algorithm.
        :return: List of tuples containing labels of visited nodes which can be cycled.
        """
        pass
