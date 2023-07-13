def breadth_first_search(graph, node):
    visited = []
    queue = []

    visited.append(node)
    queue.append(node)

    while queue:
        vertex = queue.pop(0)

        for n in graph[vertex]:
            if n not in visited:
                visited.append(n)
                queue.append(n)
    
    return visited