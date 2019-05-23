from math import radians, sin, cos, acos

# slat = Starting latitude
# slon = starting longitude
# elat = ending latitude
# elon = Ending longitude


from collections import deque, namedtuple

locations = {}
locations['Kuala Lumpur'] = {'lat':2.7456, 'lon':101.7072}
locations['Brasilia'] = {'lat':-15.8697, 'lon':-47.9172}
locations['Tokyo'] = {'lat':35.5494, 'lon':139.7798}
locations['London'] = {'lat':51.5048, 'lon':0.0495}
locations['New York'] = {'lat':40.6413, 'lon':-73.7781}
locations['Bangkok'] = {'lat':13.6900, 'lon':100.7501}
locations['Kabul'] = {'lat':34.5609, 'lon':69.2101}
#locations['California'] = {'lat':33.6762, 'lon':-117.8675} # testing purpose
destinations = ['Kuala Lumpur', 'Brasilia', 'Tokyo', 'London', 'New York', 'Bangkok', 'Kabul']

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

        path, current_vertex, d = deque(), dest, 0
        while previous_vertices[current_vertex] is not None:
            path.appendleft(current_vertex)
            d = d + calculate(locations[current_vertex]['lat'], locations[current_vertex]['lon'], locations[previous_vertices[current_vertex]]['lat'], locations[previous_vertices[current_vertex]]['lon'])
            current_vertex = previous_vertices[current_vertex]
        if path:
            path.appendleft(current_vertex)
        return pathHolder(path, d)


class pathHolder:

    def __init__(self, path, distance):
        self.path = path
        self.distance = distance
    
    def __gt__(self, holder2):
        return self.distance > holder2.distance
    
    def __str__(self):
        return '{' + str(self.distance) + '}'

    def __repr__(self):
        return str(self)
    
    def __eq__(self, holder2):
        return self.distance == holder2.distance


class MapGraph:

    def __init__(self):
        self.locations = {}
        self.locations['Kuala Lumpur'] = {'lat':2.7456, 'lon':101.7072}
        self.locations['Brasilia'] = {'lat':-15.8697, 'lon':-47.9172}
        self.locations['Tokyo'] = {'lat':35.5494, 'lon':139.7798}
        self.locations['London'] = {'lat':51.5048, 'lon':0.0495}
        self.locations['New York'] = {'lat':40.6413, 'lon':-73.7781}
        self.locations['Bangkok'] = {'lat':13.6900, 'lon':100.7501}
        self.locations['Kabul'] = {'lat':34.5609, 'lon':69.2101}
        #locations['California'] = {'lat':33.6762, 'lon':-117.8675} # testing purpose
        self.destinations = ['Kuala Lumpur', 'Brasilia', 'Tokyo', 'London', 'New York', 'Bangkok', 'Kabul']

        #initialize graph
        self.graph = Graph([])
        for i in range(len(self.destinations)):
            for j in range(i+1, len(self.destinations)):
                distance = calculate(self.locations[self.destinations[i]]['lat'], self.locations[self.destinations[i]]['lon'], self.locations[self.destinations[j]]['lat'], self.locations[self.destinations[j]]['lon'])
                self.graph.add_edge(self.destinations[i], self.destinations[j], cost=distance)
    
    def getPathsCondition(self, destination, paths, r=[]):
        print(len(paths))
        if len(r) > 3:
            return
        for i in range(0, len(r)-1):
            self.graph.remove_edge(r[i], r[i+1])
            p = self.graph.dijkstra('Kuala Lumpur', destination)
            paths.append(p)
            l = list(p.path)
            print(p.path)
            try:
                self.getPathsCondition(destination, paths, l)
            except:
                pass
            self.graph.add_edge(r[i], r[i+1], cost=calculate(self.locations[r[i]]['lat'], self.locations[r[i]]['lon'], self.locations[r[i+1]]['lat'], self.locations[r[i+1]]['lon']))
        pass

    def getPaths(self, destination):
        paths = []
        self.graph.remove_edge('Kuala Lumpur', destination)
        p = self.graph.dijkstra('Kuala Lumpur', destination)
        paths.append(p)
        l = list(p.path)
        self.getPathsCondition(destination, paths, l)
        self.graph.add_edge('Kuala Lumpur', destination, cost=calculate(self.locations['Kuala Lumpur']['lat'], self.locations['Kuala Lumpur']['lon'], self.locations[destination]['lat'], self.locations[destination]['lon']))
        paths.sort()

        #remove similiar#
        i = 0
        while i < len(paths)-1:
            if paths[i] == paths[i+1]:
                del paths[i+1]
            else:
                i += 1
        
        #print(paths)
        return paths[0:5]


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
    