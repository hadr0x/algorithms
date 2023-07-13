import unittest
from depth_first_search import depth_first_search

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
    def test_DFS(self):
        self.assertEqual(depth_first_search(graph, 0), [0, 3, 2, 4, 1, 9, 10])


if __name__ == '__main__':
    unittest.main()