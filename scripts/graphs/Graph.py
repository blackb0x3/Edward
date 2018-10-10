from typing import List, Set

import json
import os


class Node:
    """
    Base class for the graph node data structure.
    """

    def __init__(self, label: str):
        """
        Graph node constructor
        :param label: The name of the node.
        """
        self.label = label  # type: str

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

    def __init__(self, vertices: set = set(), edges: list = list(), *args, **kwargs):
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

