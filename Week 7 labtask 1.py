class undirectedgraph(object):

    def __init__(self, graph_dic={}):# initializing a graph object
        self.__graph_dic = graph_dic

    def vertices(self):
        return list(self.__graph_dic.keys()) # return the vertices of graph

    def edges(self):
        return self.__generate_edges() # return the edges of graph

    def add_node(self, node):
        if node not in self.__graph_dic:# if node not in list an empty vertex added to dic
            self.__graph_dic[node] = []

    def add_edge(self, edge):
        edge = set(edge)
        (node1, node2) = tuple(edge)
        if node1 in self.__graph_dic:
            self.__graph_dic[node1].append(node2)
        else:
            self.__graph_dic[node1] = [node2]

    def __generate_edges(self):
        edges = []
        for node in self.__graph_dic:
            for neighbour in self.__graph_dic[node]:
                if {neighbour, node} not in edges:
                    edges.append({node, neighbour})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dic:
            res += str(k) + " " # method for generating graph edges
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":
    
    g = { "A" : ["C", "B"],
          "B" : ["A", "C"],
          "C" : ["B", "D"],
          "D" : ["C", "E"],
          "E" : ["D", "F"],
          "F" : ["E"]
         } 

    graph = undirectedgraph(g)

    print("Graph Vertices ="),(graph.vertices())

    print("Graph Edges ="),(graph.edges())

    print("Adding an Vertex:")
    graph.add_node("H")

    print("Graph Vertices ="),(graph.vertices())

    print("Adding an Edge:")
    graph.add_edge({"D","G"})
    
    print("Graph Edges ="),(graph.edges())

    print('Adding an Edge {"H","L"} with new vertices:')
    graph.add_edge({"H","L"})

    print("Graph Edges ="),(graph.edges())
