def mult2(n):
    return n * 2


num = 50

print(mult2(num))


def mult2_list(l):
    list2 = [(n * 2) for n in l]
    return list2


print(mult2_list([4, 6, 2, 67, 7, 0]))
# y = [(x+1) for x in range(5)]
