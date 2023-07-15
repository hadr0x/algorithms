def depth_first_search(graph, vertex, visited = list()):

    if vertex not in visited:
        visited.append(vertex)
        for n in graph[vertex]:
            depth_first_search(graph, n)

    return visited