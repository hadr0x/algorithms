import unittest
from breadth_first_search import breadth_first_search

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
    def test_BFS(self):
        self.assertEqual(breadth_first_search(root), [0, 3, 9, 2, 1, 10, 4])
        self.assertEqual(breadth_first_search(root.left), [3, 2, 1, 4])


if __name__ == '__main__':
    unittest.main()