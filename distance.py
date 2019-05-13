from math import radians, sin, cos, acos

# slat = Starting latitude
# slon = starting longitude
# elat = ending latitude
# elon = Ending longitude


from collections import deque, namedtuple


# we'll use infinity as a default distance to nodes.
inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')


def make_edge(start, end, cost=1):
  return Edge(start, end, cost)


class Graph:
    def __init__(self, edges):
        # let's check that the data is right
        wrong_edges = [i for i in edges if len(i) not in [2, 3]]
        if wrong_edges:
            raise ValueError('Wrong edges data: {}'.format(wrong_edges))

        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )

    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost=1, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if [edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1, n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbours(self):
        neighbours = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbours[edge.start].add((edge.end, edge.cost))

        return neighbours

    def dijkstra(self, source, dest):
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        while vertices:
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            if distances[current_vertex] == inf:
                break
            for neighbour, cost in self.neighbours[current_vertex]:
                alternative_route = distances[current_vertex] + cost
                if alternative_route < distances[neighbour]:
                    distances[neighbour] = alternative_route
                    previous_vertices[neighbour] = current_vertex

        path, current_vertex = deque(), dest
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return path


def calculate(lat1, lon1, lat2, lon2):
    slat = radians(float(lat1))
    slon = radians(float(lon1))
    elat = radians(float(lat2))
    elon = radians(float(lon2))
    dist = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
    #print("The distance is %.2fkm." % dist)
    return dist


if __name__ == '__main__':

    print("kl to Brasilia")
    calculate(2.7456, 101.7072, -15.8697, -47.9172)
    print("kl to tokyo")
    calculate(2.7456, 101.7072, 35.5494, 139.7798)
    print("kl to London")
    calculate(2.7456, 101.7072, 51.5048, 0.0495)
    print("kl to New York")
    calculate(2.7456, 101.7072, 40.6413, -73.7781)
    print("kl to Bangkok")
    calculate(2.7456, 101.7072, 13.6900, 100.7501)
    print("kl to Kabul")
    calculate(2.7456, 101.7072, 34.5609, 69.2101)

    print("Brasilia to tokyo")
    calculate(-15.8697, -47.9172, 35.5494, 139.7798)
    print("Brasilia to London")
    calculate(-15.8697, -47.9172, 51.5048, 0.0495)
    print("Brasilia to New York")
    calculate(-15.8697, -47.9172, 40.6413, -73.7781)
    print("Brasilia to Bangkok")
    calculate(-15.8697, -47.9172, 13.6900, 100.7501)
    print("Brasilia to Kabul")
    calculate(-15.8697, -47.9172, 34.5609, 69.2101)

    print("Tokyo to London")
    calculate(35.5494, 139.7798, 51.5048, 0.0495)
    print("Tokyo to New York")
    calculate(35.5494, 139.7798, 40.6413, -73.7781)
    print("Tokyo to Bangkok")
    calculate(35.5494, 139.7798, 13.6900, 100.7501)
    print("Tokyo to Kabul")
    calculate(35.5494, 139.7798, 34.5609, 69.2101)

    print("London to New York")
    calculate(51.5048, 0.0495, 40.6413, -73.7781)
    print("London to Bangkok")
    calculate(51.5048, 0.0495, 13.6900, 100.7501)
    print("London to Kabul")
    calculate(51.5048, 0.0495, 34.5609, 69.2101)

    print("New York to Bangkok")
    calculate(40.6413, -73.7781, 13.6900, 100.7501)
    print("New York to Kabul")
    calculate(40.6413, -73.7781, 34.5609, 69.2101)

    print("Bangkok to Kabul")
    calculate(13.6900, 100.7501, 34.5609, 69.2101)

    graph = Graph([
        ("a", "b", 7),  ("a", "c", 9),  ("a", "f", 14), ("b", "c", 10),
        ("b", "d", 15), ("c", "d", 11), ("c", "f", 2),  ("d", "e", 6),
        ("e", "f", 9),("a", "e", 7)])

    print(graph.dijkstra("a", "e"))
    graph.remove_edge("a", "e")
    a = graph.dijkstra("a", "d")
    print(a)
    while len(a) > 0:
        print(a.popleft())
    b = "abcd"
    print(b[0:-1])
    