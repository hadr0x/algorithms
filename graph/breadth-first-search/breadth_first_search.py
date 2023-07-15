from collections import deque

def breadth_first_search(graph, start):
    list = []
    queue = deque()

    list.append(start)
    queue.append(start)

    while queue:
        vertex = queue.popleft()

        for n in graph[vertex]:
            if n not in list:
                list.append(n)
                queue.append(n)
    
    return list