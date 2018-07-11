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
