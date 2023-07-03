def depth_first_search(graph, node, visited=[]):

    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            depth_first_search(graph, n)

    return visited