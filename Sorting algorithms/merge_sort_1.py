import unittest


def merge(a, b):
    """
    It Accepts 2 sorted arrays and returns 1
    """
    c = [0 for _ in range(len(a) + len(b))]
    i = k = n = 0
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1

    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1
    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1
    return c


def merge_sort(a):
    """
    It divides the array into 2 parts and calls "merge" to merge into 1 array
    """
    if len(a) <= 1:
        return
    middle = len(a) // 2
    l = a[:middle]
    r = a[middle:]
    merge_sort(l)
    merge_sort(r)
    c = merge(l, r)
    for i in range(len(a)):
        a[i] = c[i]


class TestCall(unittest.TestCase):
    def test_example_1(self):
        a = [5, 1, 3, 8, 9, 20, 90, 2, 7, 5]
        merge_sort(a)
        self.assertEqual(a, [1, 2, 3, 5, 5, 7, 8, 9, 20, 90])

    def test_example_2(self):
        a = [1, 1, 1, 2, 1, 1, 1, 1]
        merge_sort(a)
        self.assertEqual(a, [1, 1, 1, 1, 1, 1, 1, 2])

    def test_example_3(self):
        a = [1, 1, 1, 1, 1, 1, 1, 1]
        merge_sort(a)
        self.assertEqual(a, [1, 1, 1, 1, 1, 1, 1, 1])

    def test_example_4(self):
        a = [1]
        merge_sort(a)
        self.assertEqual(a, [1])


if __name__ == '__main__':
    unittest.main()
