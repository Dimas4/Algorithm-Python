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
