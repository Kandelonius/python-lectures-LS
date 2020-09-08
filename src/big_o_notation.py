my_list = [1, 2, 3, 4, 5]
longer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def print_list(arr):  # O(n) linear
    for n in arr:
        print(n)


print_list(my_list)


def print_pairs(items):  # O(n^2) quadratic
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)


def my_func(arr):
    a = 1
    b = 2
    c = a * b

    for x in range(1000):
        print(x)

    for thing in arr:
        x = 10
        y = 20
        z = x * y
        print(thing)


my_func(my_list)
my_func(longer_list)


# "on the order of"

def two_loops(arr):  # still O(n) linear
    for x in range(1000000000):
        z = x * x
        print(z)

    for thing in arr:
        print(thing)

    for thing_again in arr:
        print(thing_again)


# def simple_recurse(n):
#     if n <= 1:
#         return n
#     simple_recurse(n)
#
# def weird_recurse(num):
#     if n <= 1:
#         return num
#     simple_recurse(num - 1)
#     simple_recurse(num - 1)
#     simple_recurse(num - 1)
def two_n_demo(n):
    if n == 0:
        return 1
    a = two_n_demo(n - 1)
    b = two_n_demo(n - 1)
    return a + b


two_n_demo(3)
