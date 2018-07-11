import unittest


def quick_sort(array):
    """
    It takes the array and divides it into 3 others: less, equal and more
    Then do this for each of these arrays.
    """
    less = []
    equal = []
    more = []
    if len(array) > 1:
        element = array[0]
        for i in array:
            if i < element:
                less.append(i)
            if i == element:
                equal.append(i)
            if i > element:
                more.append(i)
        return quick_sort(less) + equal + quick_sort(more)
    return array


class TestCall(unittest.TestCase):
    def test_example_1(self):
        a = [1, 4, 3, 3, 2, 5, 1, 4, 3, 1, 2, 5,  4, 5]
        a = quick_sort(a)
        self.assertEqual(a, [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])

    def test_example_2(self):
        a = [1, 1, 1, 2, 1, 1, 1, 1]
        a = quick_sort(a)
        self.assertEqual(a, [1, 1, 1, 1, 1, 1, 1, 2])

    def test_example_3(self):
        a = [1, 1, 1, 1, 1, 1, 1, 1]
        a = quick_sort(a)
        self.assertEqual(a, [1, 1, 1, 1, 1, 1, 1, 1])

    def test_example_4(self):
        a = [1]
        a = quick_sort(a)
        self.assertEqual(a, [1])


if __name__ == '__main__':
    unittest.main()
