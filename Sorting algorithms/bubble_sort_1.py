import unittest


def bubble_sort(array):
    """
    It compares 2 elements in an array and moves them if it's needed
    """
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


class TestCall(unittest.TestCase):
    def test_example_1(self):
        a = [5, 1, 3, 8, 9, 20, 90, 2, 7, 5]
        bubble_sort(a)
        self.assertEqual(a, [1, 2, 3, 5, 5, 7, 8, 9, 20, 90])

    def test_example_2(self):
        a = [1, 1, 1, 2, 1, 1, 1, 1]
        bubble_sort(a)
        self.assertEqual(a, [1, 1, 1, 1, 1, 1, 1, 2])

    def test_example_3(self):
        a = [1, 1, 1, 1, 1, 1, 1, 1]
        bubble_sort(a)
        self.assertEqual(a, [1, 1, 1, 1, 1, 1, 1, 1])

    def test_example_4(self):
        a = [1]
        bubble_sort(a)
        self.assertEqual(a, [1])


if __name__ == '__main__':
    unittest.main()
