import unittest
from treeTraversals import inorder, postorder, preorder

# Node constructor
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Tree implementation

root = Node(0)                      # 0
root.left = Node(3)                 # ├── 3
root.right = Node(9)                # │   ├── 2
root.left.left = Node(2)            # │   │   └── 4
root.left.right = Node(1)           # │   └── 1
root.left.left.left = Node(4)       # └── 9
root.right.left = Node(10)          #     └── 10

class Test(unittest.TestCase):
    def test_inorder(self):
        self.assertEqual(inorder(root), [4, 2, 3, 1, 0, 10, 9])

    def test_preorder(self):
        self.assertEqual(preorder(root), [0, 3, 2, 4, 1, 9, 10])

    def test_postorder(self):
        self.assertEqual(postorder(root), [4, 2, 1, 3, 10, 9, 0])


if __name__ == '__main__':
    unittest.main()