def checker(array, check=True):
    s = 2 * int(check) - 1
    for i in range(1, len(array)):
        if s * array[i] < s * array[i-1]:
            return False
    return True


array_1 = [1, 2, 3, 4]
array_2 = [1, 2, 5, 4]
array_3 = [5, 4, 3, 2]


print(checker(array_1))
print(checker(array_2))
print(checker(array_3, False))
