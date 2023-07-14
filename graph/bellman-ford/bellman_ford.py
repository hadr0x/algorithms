class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def display_distances(self, dist):
        for i in range(len(dist)):
            print("Distance from vertex 0 to vertex", i, "is", dist[i])

    def bellman_ford(self, src):
        dist = [float('inf')] * self.v
        dist[src] = 0

        # Relax edges |v| - 1 times
        for _ in range(self.v - 1):
            for u, v, w in self.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # Detect negative cycle
        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return
        return self.display_distances(dist)