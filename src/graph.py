class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, **pos): # TODO: Test default value arguments
        self.value = value
        self.color = 'pink'
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('T1', x = 40, y = 40)
        debug_vertex_2 = Vertex('T2', x = 200, y = 300)
        debug_vertex_3 = Vertex('T3', x = 100, y = 475)
        debug_vertex_4 = Vertex('T4', x = 488, y = 400)

        debug_edge_1 = Edge(debug_vertex_2)        
        debug_vertex_1.edges.append(debug_edge_1)

        debug_edge_2 = Edge(debug_vertex_2)
        debug_vertex_3.edges.append(debug_edge_2)

        # debug_edge_3 = Edge(debug_vertex_3)
        # debug_vertex_4.edges.append(debug_edge_3)

        self.vertexes.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4])