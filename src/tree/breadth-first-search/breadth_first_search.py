def breadth_first_search(root):
    visited = []
    queue = []

    queue.append(root)

    while queue:
        node = queue.pop(0)
        visited.append(node.data)

        if node.left != None:
            queue.append(node.left)
        
        if node.right != None:
            queue.append(node.right)

    return visited