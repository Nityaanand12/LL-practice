class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False
    
    def print_vertex(self):
        for i in self.adj_list.items():
            print(f"{i[0]} : {i[1]}")
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            if v2 in self.adj_list[v1]:
                self.adj_list[v1].remove(v2)
            if v1 in self.adj_list[v2]:
                self.adj_list[v2].remove(v1)
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in  self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


mygraph = Graph()
mygraph.add_vertex('A')
mygraph.add_vertex('B')
mygraph.add_vertex('C')
mygraph.add_edge('A', 'B')
mygraph.remove_edge('A', 'B')
mygraph.add_edge('A', 'C')
mygraph.remove_vertex('C')
mygraph.print_vertex()
        
