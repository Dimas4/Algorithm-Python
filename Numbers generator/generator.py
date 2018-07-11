import time


def gen_str(deep, string=None):
    if deep == 0:
        return
    string = string or []
    gen_str(deep-1, string.append(0))
    gen_str(deep-1, string.append(1))
    gen_str(deep-1, string.append(2))
    gen_str(deep-1, string.append(3))
    gen_str(deep-1, string.append(4))


start = time.time()
gen_str(5)
print(time.time() - start)


def generator(system, deep, array=None):
    if deep == 0:
        print(array)
        return
    array = array or []
    for i in range(system):
        array.append(i)
        generator(system, deep-1, array)
        array.pop()


start = time.time()
generator(5, 5)
print(time.time() - start)

