def method_1(weight, value):
    coefficient = [(value[i]/weight[i]) for i in range(len(weight))]
    sum = 0
    ind_take = 0
    for i in range(len(weight)):
        if sum > 10:
            break
        ind = m = 0
        for j in range(len(weight)):
            if coefficient[j] > m:
                m = coefficient[j]
                sum += weight[j]
                ind = j
        value[ind_take] = ind
        ind_take += 1
        coefficient[ind] = -1

    value = value[:ind_take]
    return value


def method_2(weight, value):
    string = "0" * len(weight)
    while len(string) != len(weight):
        string = int(string)+1
        string = str(string)
        if '2' in string or '3' in string or '4' in string or '5' in string or '6' in string or \
                '7' in string or '8' in string or '9' in string:
            continue
        print(string)


weight = [3, 4, 4, 5]
value = [4, 5, 6, 6]
print(method_1(weight, value))
print(method_2(weight, value))
