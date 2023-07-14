from queue import PriorityQueue

class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.edges = [[-1 for i in range(vertices)] for j in range(vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight

    def display_distances(self, dist):
        for i in range(len(dist)):
            print("Distance from vertex 0 to vertex", i, "is", dist[i])


    def dijkstra(self, start_vertex):
        dist = {v:float('inf') for v in range(self.v)}
        dist[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (_, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = dist[neighbor]
                        new_cost = dist[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            dist[neighbor] = new_cost
        
        return self.display_distances(dist)