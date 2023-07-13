# Inorder Traversal : left --> root --> right
def inorder(node, list=[]):
    if node:
        inorder(node.left)
        list.append(node.data)
        inorder(node.right)
    return list


# Preorder Traversal : root --> left --> right
def preorder(node, list=[]):
    if node:
        list.append(node.data)
        preorder(node.left)
        preorder(node.right)
    return list


# Postorder Traversal : left --> right --> root
def postorder(node, list=[]):
    if node:
        postorder(node.left)
        postorder(node.right)
        list.append(node.data)
    return list