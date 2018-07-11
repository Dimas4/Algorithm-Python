import unittest


def counting_sort(sort_len, array):
    """
    It takes the number of different elements in an array (sort_len) and an array
    After that, it creates a new array (sort_array), collects data from sort_array
    to array
    """
    sort_array = [0 for _ in range(sort_len+1)]

    for i in array:
        sort_array[i] += 1

    index = 0
    for ind in range(sort_len+1):
        while sort_array[ind] != 0:
            array[index] = ind
            index += 1
            sort_array[ind] -= 1


class TestCall(unittest.TestCase):
    def test_example_1(self):
        a = [1, 4, 3, 3, 2, 5, 1, 4, 3, 1, 2, 5,  4, 5]
        counting_sort(5, a)
        self.assertEqual(a, [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5])

    def test_example_2(self):
        a = [1, 1, 1, 2, 1, 1, 1, 1]
        counting_sort(2, a)
        self.assertEqual(a, [1, 1, 1, 1, 1, 1, 1, 2])

    def test_example_3(self):
        a = [1, 1, 1, 1, 1, 1, 1, 1]
        counting_sort(1, a)
        self.assertEqual(a, [1, 1, 1, 1, 1, 1, 1, 1])

    def test_example_4(self):
        a = [1]
        counting_sort(1, a)
        self.assertEqual(a, [1])


if __name__ == '__main__':
    unittest.main()
