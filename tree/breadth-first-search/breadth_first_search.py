from collections import deque

def breadth_first_search(root):
    list = []
    queue = deque()

    queue.append(root)

    while queue:
        node = queue.popleft()
        list.append(node.data)

        if node.left != None:
            queue.append(node.left)
        
        if node.right != None:
            queue.append(node.right)

    return list