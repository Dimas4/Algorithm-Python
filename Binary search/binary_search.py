def search(target, left, right, array):
    middle = (left + right)//2
    element = array[middle]
    if element == target:
        return middle
    if left >= right:
        return False
    elif element > target:
        return search(target, left, middle-1, array)
    elif element < target:
        return search(target, middle+1, right, array)


def search_for(target, array):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        if array[middle] > target:
            right = middle - 1
        elif array[middle] < target:
            left = middle + 1
    return False


array = [1, 2, 3, 4, 5]
print(search(9, 0, len(array)-1, array))
print(search_for(10, array))
