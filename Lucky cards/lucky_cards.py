cards = ['124133', '777597', '123789', '5557339']

for i in cards:
    card_len = len(i) - 1
    first_part = i[:(card_len+1)//2]
    second_part = i[card_len//2+1:]
    f_s_zip = zip(first_part, second_part)
    sum_f = sum_s = 0
    for f, s in f_s_zip:
        sum_f += int(f)
        sum_s += int(s)
    if sum_f == sum_s:
        print(f'{i} lucky card!')


