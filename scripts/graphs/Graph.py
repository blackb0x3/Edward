from scripts.Algorithm import Algorithm, AlgorithmError

from datetime import datetime
from itertools import permutations, combinations
from typing import List, Set

import json
import os
import random


class Node:
    """
    Base class for the graph node data structure.
    """

    def __init__(self, label: str):
        """
        Graph node constructor
        :param label: The name of the node.
        """
        self.label = label   # type: str
        self.visited = False # type: bool

    def __eq__(self, other):
        """
        Overrides the default implementation.
        :param other: Comparing Node object.
        :return: True if equal, False otherwise.
        """
        if isinstance(other, Node):
            return self.label == other.label

        return False

    def __str__(self):
        """
        Overrides default implementation.
        """

        to_return = " _ _ _" + os.linesep
        to_return += "|     |" + os.linesep
        to_return += "|  " + self.label + "  |" + os.linesep
        to_return += "|_ _ _|" + os.linesep

        return to_return

    def json(self):
        """
        Exports the Node object into a JSON serializable object.
        :return: The serialized Node object in JSON format.
        """

        return json.dumps(self.__dict__)


class Edge:
    """
    Base class for the graph edge data structure.
    """

    def __init__(self, source: Node, destination: Node, distance: float, *args, **kwargs):
        """
        Graph edge constructor
        :param source: The start node.
        :param destination: The end node.
        :param distance: The distance between the source and destination nodes.
        :raises ValueError: If the source and destination nodes are the same.
        """

        if source == destination:
            raise ValueError("The source and destination nodes cannot be the same.")

        self.source = source
        self.destination = destination
        self.distance = distance

        self.directional = kwargs.get("direction", False)

    def __eq__(self, other):
        """
        Overrides the default implementation.
        :param other: Comparing Edge object.
        :return: True if equal, False otherwise.
        """
        if isinstance(other, Edge):
            return (self.source == other.source and
                    self.destination == other.destination and
                    self.distance == other.distance and
                    self.directional == other.directional)

        return False

    def __str__(self):
        """
        Overrides default implementation.
        """

        to_return = " _ _ _         _ _ _" + os.linesep
        to_return += "|     |       |     |" + os.linesep
        to_return += "|  " + self.source.label + "  | ==== " + self.distance + " ==== |  " + self.destination.label + "  |" + os.linesep
        to_return += "|_ _ _|       |_ _ _|" + os.linesep

        return to_return

    def json(self):
        """
        Exports the Edge object into a JSON serializable object.
        :return: The serialized Edge object in JSON format.
        """

        return json.dumps(self.__dict__)


class Graph:
    """
    Base class for the graph data structure.
    """

    def __init__(self, vertices: set = set(), edges: set = set(), *args, **kwargs):
        """
        Graph constructor
        :param vertices: The set of points on the graph.
        :param edges: The connections between the vertices.
        :param args: args
        :param kwargs: kwargs
        """

        self.vertices = vertices  # type: Set[Node]
        self.edges = edges        # type: Set[Edge]

    def add_edge(self, edge: Edge = None, src: Node = None, dest: Node = None, dist: float = None, dir: bool = False):
        """
        Adds a new connection between two nodes in the graph.
        :param edge: An instantiated Edge object.
        :param source: The start node.
        :param destination: The end node.
        :param distance: The distance between the source and destination nodes.
        :return: True if the Edge was added, False otherwise.
        :raises: ValueError: If no parameters are provided.
        """

        if edge is not None:
            if (edge.source in self.vertices and
                    edge.destination in self.vertices):
                return self.edges.add(edge)
        elif src is not None and dest is not None and dist is not None:
            if (src in self.vertices and
                    dest in self.vertices and
                    src != dest):
                return self.edges.add(Edge(src, dest, dist, dir))
        else:
            raise ValueError("You must provide an Edge, or components of an edge (source, destination and distance)")

    def remove_edge(self, edge: Edge = None, src: Node = None, dest: Node = None, dist: float = None, dir: bool = False):
        """
        Removes an existing connection between two nodes in the graph.
        :param edge: An instantiated Edge object.
        :param src: The start node.
        :param dest: The end node.
        :param dist: The distance between the source and destination nodes.
        :return: True if the Edge was removed, False otherwise.
        :raises: ValueError: If no parameters are provided.
        """

        if edge is not None:
            if edge in self.edges:
                return self.edges.remove(edge)

            return False

        elif src is not None and dest is not None and dist is not None:
            potential_edge = Edge(src, dest, dist, dir)

            if potential_edge in self.edges:
                return self.edges.remove(potential_edge)

            return False

        else:
            raise ValueError("You must provide an Edge, or components of an edge (source, destination and distance)")

    def __eq__(self, other):
        """
        Overrides the default equality operator.
        :param other: The other graph to compare.
        :return: True if the two graphs are equal, False otherwise.
        """

        if isinstance(other, Graph):
            return (self.vertices == other.vertices and
                self.edges == other.edges)


        return False

    def __str__(self):
        """
        Overrides default implementation.
        """

        to_return = "VERTICES" + os.linesep + os.linesep

        for vertex in self.vertices:
            to_return += str(vertex) + os.linesep

        to_return += "EDGES" + os.linesep + os.linesep

        for edge in self.edges:
            to_return += str(edge) + os.linesep

    def json(self):
        """
        Exports the Graph object into a JSON serializable object.
        :return: The serialized Graph in JSON format.
        """

        return json.dumps(self.__dict__)

    def dict_edges(self):
        """
        Converts the list of edges into a dictionary.
        Useful for algorithms which require the use of
        a dictionary to iterate over visited nodes in the graph.
        """

        to_return = dict()

        for edge in self.edges:
            if edge.source.label not in to_return.keys():
                to_return.update({edge.source.label: set()})
            to_return[edge.source.label].add(edge.destination.label)

        return to_return


class GraphAlgorithm(Algorithm):
    """
    Base class for algorithms involving graphs.
    """

    def __init__(self, *args, **kwargs):
        self.output = list()
        super().__init__(self, args, kwargs)

    def generate_collection(self, *args, **kwargs):
        """
        Generates a graph for a cyclic detection algorithm.
        :param args: Ordered list of args.
        :param kwargs: Keyword args.
        :return: The generated graph.
        """

        nodes = set(kwargs.get('nodes', set()))

        # generate nodes if none are provided
        if len(nodes) == 0:
            # pre-calculated permutations of picking alphabet characters - 27/10/2018
            one_char_comb = 26
            two_char_comb = 325
            three_char_comb = 2600

            node_count = kwargs.get('node_count', 5)
            alpha_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            possible_nodes = []

            # no. of combinations of picking 1 character from the alpphabet
            if node_count <= one_char_comb:
                possible_nodes = ["".join(p) for p in combinations(alpha_string[:node_count], 1)]

            # no. of combinations of picking 2 characters
            elif node_count <= two_char_comb:
                possible_nodes = ["".join(p) for p in combinations(alpha_string, 2)]

            # no. of combinations of picking 3 characters
            elif node_count <= three_char_comb:
                possible_nodes = ["".join(p) for p in combinations(alpha_string, 3)]

            else:
                raise AlgorithmError(self, msg="Node count is too high, maximum number of node is 2600")

            while node_count > 0:
                nodes.add(Node(label=possible_nodes.pop(random.randrange(0, node_count))))
                node_count -= 1
        else:
            nodes = set([Node(label=node) for node in nodes])

        edges = set(kwargs.get('edges', set()))

        self.oldcollection = Graph(vertices=nodes, edges=edges)

    def collection_is_valid(self):
        """
        Determines if the collection is valid for this algorithm.
        In this case, a Graph.
        :return: True if the collection is a Graph, False otherwise.
        """

        return isinstance(self.oldcollection, Graph)

    def __dict__(self):
        """
        Overrides the default implementation.
        """

        return {
            "successful_execution": self.executed,
            "input": self.oldcollection.json(),
            "output": self.output.__dict__,
            "execution_start": self.starttime.strftime("%Y-%m-%d %H:%M:%S"),
            "execution_end": self.endtime.strftime("%Y-%m-%d %H:%M:%S"),
            "execution_time": str(self.timetaken)
        }

    def has_worked(self):
        """
        Determines if the algorithm worked or not.
        """

        raise NotImplementedError("Please use a specific graph algorithm's has_worked() function.")

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
