from typing import List, Set


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
