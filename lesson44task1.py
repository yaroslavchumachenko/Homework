from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.transposed_graph = defaultdict(list)
        self.visited = [False] * self.V
        self.stack = []
        self.scc = []

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.transposed_graph[v].append(u)

    def dfs(self, v):
        self.visited[v] = True
        for i in self.graph[v]:
            if not self.visited[i]:
                self.dfs(i)
        self.stack.append(v)

    def dfs_transposed(self, v):
        self.visited[v] = True
        self.scc[-1].append(v)
        for i in self.transposed_graph[v]:
            if not self.visited[i]:
                self.dfs_transposed(i)

    def get_strongly_connected_components(self):
        for i in range(self.V):
            if not self.visited[i]:
                self.dfs(i)

        self.visited = [False] * self.V
        while self.stack:
            v = self.stack.pop()
            if not self.visited[v]:
                self.scc.append([])
                self.dfs_transposed(v)
        
        return self.scc

if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print(g.get_strongly_connected_components())
