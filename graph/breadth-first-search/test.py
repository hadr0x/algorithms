import unittest
from breadth_first_search import breadth_first_search

graph = {
    0 : [3, 9],
    3 : [2, 1],
    9 : [10],
    2 : [4],
    4 : [],
    1 : [],
    10 : []
}

class Test(unittest.TestCase):
    def test_BFS(self):
        self.assertEqual(breadth_first_search(graph, 0), [0, 3, 9, 2, 1, 10, 4])
        self.assertEqual(breadth_first_search(graph, 3), [3, 2, 1, 4])

if __name__ == '__main__':
    unittest.main()