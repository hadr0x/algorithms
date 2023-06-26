import unittest
from bubbleSort import bubbleSort

unorderedArray = [25, 12, 29, 4, 30, 8, 19, 28, 1, 9, 2]
orderedArray = [1, 3, 5, 6, 7, 9, 11, 14, 18, 24, 28, 30]
reversedArray = [30, 27, 23, 20, 17, 14, 11, 9, 6, 5, 2, 1]
equalArray = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
negativeArray = [-12, -3, -19, -30, -7, -1, -23, -20]
negativeorderedArray = [-30, -25, -21, -17, -12, -9, -5, -2, -1]


class testSort(unittest.TestCase):
    def test_bubbleSort(self):
        self.assertEqual(bubbleSort(unorderedArray), [1, 2, 4, 8, 9, 12, 19, 25, 28, 29, 30])
        self.assertEqual(bubbleSort(negativeArray), [-30, -23, -20, -19, -12, -7, -3, -1])




if __name__ == '__main__':
    unittest.main()