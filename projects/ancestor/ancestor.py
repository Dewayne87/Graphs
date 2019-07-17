class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    ## initial pull request
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            self.add_vertex(v1)
        if v2 not in self.vertices:
            self.add_vertex(v2)
        self.vertices[v1].add(v2)
    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            node = q.dequeue()
            if node not in visited:
                visited.add(node)
                print(node)
                for edge in self.vertices[node]:
                    q.enqueue(edge)
                    

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size() > 0:
            node = s.pop()
            if node not in visited:
                visited.add(node)
                print(node)
                for edge in self.vertices[node]:
                    s.push(edge)
    def dft_recursive(self, node,visited = set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        
        if node not in visited:
            visited.add(node)
            print(node)
            for edge in self.vertices[node]:
                self.dft_recursive(edge,visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        q.enqueue([starting_vertex])
        while q.size() > 0:
            path = q.dequeue()
            node = path[-1]
            if node == destination_vertex:
                return path
            for edge in self.vertices[node]:
                copy_path = path[:] ## necessary for correct path
                copy_path.append(edge)
                q.enqueue(copy_path)
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        s.push([starting_vertex])
        while s.size() > 0:
            path = s.pop()
            node = path[-1]
            if node == destination_vertex:
                return path
            for edge in self.vertices[node]:
                copy_path = path[:]
                copy_path.append(edge)
                s.push(copy_path)


def earliest_ancestor(ancestors, starting_node):
    pass