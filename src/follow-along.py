import math
def spam(n):
    i = 1
    while i < n:
        print(i)
        i *= 2

spam(100)

def eggs(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)

eggs(10)

def bacon(n):
    sum = 0
    for i in range(0, 1463):
        i += 1
        for j in range(0, n):
            for k in range(n, n+15):
                sum += 1
bacon(10)

def sausage(array):
    print(array[1])
    midpoint = len(array) // 2
    for i in range(0, midpoint):
        print(array[i])
        for _ in range(1000):
            print('hi')

print("follow")
list1 = [1,2,4]
list2 = [1,3,5]

list1.extend(list2)
combined = list(set(list1))

print(combined)