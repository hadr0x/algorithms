def DFS(visited, graph, node):

    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            DFS(visited, graph, n)

    return visited