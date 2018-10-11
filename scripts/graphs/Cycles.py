from scripts.graphs.Graph import Edge, Graph, Node, GraphAlgorithm
from scripts.Algorithm import AlgorithmError

from datetime import datetime
import networkx as nx


class DetectCycleAlgorithm(GraphAlgorithm):
    """
    Class of algorithms which detect if there is at least one cycle in the provided graph.
    """

    def run(self):
        """
        Performs algorithm's pre-execution and post-execution steps.
        Overrides the default implementation by storing detected cycles in self.newcollection.
        """

        try:
            if self.executed is False:
                self.newcollection = set()
                self.starttime = datetime.now()
                self.execute()
                self.executed = self.has_worked()
                self.endtime = datetime.now()
                self.timetaken = self.endtime - self.starttime
        except AlgorithmError as err:
            print("Algorithm runtime error: ", err)
        except RuntimeError as run_err:
            print("Error: ", run_err)

    def has_worked(self):
        """
        Determines if the algorithm correctly detected cycles in the graph, as intended.
        :raise: AlgorithmError if a cycle was detected where there isn't one, or vice versa.
        :return: True if the algorithm detected the correct number of cycles.
        """

        g = nx.Graph()

        for edge in self.oldcollection.edges:
            g.add_edge(edge.source.label, edge.destination.label, weight=edge.distance)

        if len(list(nx.simple_cycles(g))) != len(self.newcollection):
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
