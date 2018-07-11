field = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

field_len = len(field)

for i in range(1, field_len):
    for j in range(1, field_len):
        if i == j == 1:
            continue
        field[i][j] = field[i][j-1] + field[i-1][j]

for i in field:
    print(i)

