def max_sequence(A1, A2):
    F = [[0 for _ in range(len(A2)+1)] for _ in range(len(A1)+1)]
    for i in range(1, len(A1)+1):
        for j in range(1, len(A2)+1):
            if A1[i-1] == A2[j-1]:
                F[i][j] = 1 + F[i-1][j-1]
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[-1][-1]


A1 = [1, 2, 3, 9]
A2 = [1, 5, 3, 18, 26, 9]
a = max_sequence(A1, A2)
print(a)
