def max_sequence(A):
    array = [0 for _ in range(len(A))]
    for i in range(len(A)):
        max = 0
        for j in range(i):
            if A[i] > A[j] and array[j] > max:
                max = array[j]
        array[i] = 1 + max
    return array[-1]


array1 = [1, 5, 9, 1, 2, 15]

print(max_sequence(array1))
