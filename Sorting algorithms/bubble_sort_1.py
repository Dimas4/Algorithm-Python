def bubble_sort(array):
    """
    It compares 2 elements in an array and moves them if it's needed
    """
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
