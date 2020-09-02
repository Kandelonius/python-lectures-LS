# Space complexity: O(len(arrA) + len(arrB))
# Space complexity: O(n + m)

def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    arrA_idx = 0
    arrB_idx = 0

    # loop over the merged_arr
    for idx in range(elements):
        # check if we are at the end of one of the arrays
        # if so, just use other array
        if arrA_idx >= len(arrA):
            merged_arr[idx] = arrB[arrB_idx]
            arrB_idx += 1

        elif arrB_idx >= len(arrB):
            merged_arr[idx] = arrA[arrA_idx]
            arrA_idx += 1

        # compare the first element of each array
        # smaller element goes into merged array
        elif arrA[arrA_idx] < arrB[arrB_idx]:
            merged_arr[idx] = arrA[arrA_idx]

            arrA_idx += 1
        else:
            merged_arr[idx] = arrB[arrB_idx]
            arrB_idx += 1

    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    else:
        mid = len(arr) // 2
        # recurse on left half
        left = merge_sort(arr[:mid])
        # recurse on right half
        right = merge_sort(arr[mid:])
        # put things back together: merge
        arr = merge(left, right)

    return arr


# instead of new array, let's swap stuff
# (x,y = y,x)
#  v        v
# [4, 5, 6, 1, 3, 7]

#     v        v
# [1, 4, 5, 6, 3, 7]

#        v        v
# [1, 3, 4, 5, 6, 7]


def merge_in_place(arr, start, mid, end):
    start2 = mid + 1

    if (arr[mid] <= arr[start2]):
        return arr

    while start <= mid and start2 <= end:

        # what if start < start2?
        if arr[start] < arr[start2]:
            start += 1

        else:
            # save the second item and its index
            value = arr[start2]
            idx = start2
            # shift everything over one at a time
            while idx != start:
                # move left neighbor to the right one step
                arr[idx] = arr[idx - 1]
                idx -= 1

            # move the second item over
            arr[start] = value

            # update our counters
            start += 1
            start2 += 1
            mid += 1

    return arr


# Space complexity: O(1)
def merge_sort_in_place(arr, left, right):
    # what's our base case?
    ## if the right less than the left
    if right <= left:
        return arr

    else:
        # find middle
        middle = (right + left) // 2
        ## recurse on left and right halves
        merge_sort_in_place(arr, left, middle)
        merge_sort_in_place(arr, middle + 1, right)

        merge_in_place(arr, left, middle, right)

    return arr


##### fibbonacci

# 0 1 1 2 3 5 8 13 21 34 55

# Memoization, "caching"
# Top-Down Dynamic Programming

cache = {}


def fib(n):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n - 1) + fib(n - 2)

    return cache[n]


for i in range(1000000):
    print(f"{i}: {fib(i)}")

d = {
    "foo": 12,
    "bar": 17,
    "qux": 2,
    # 34: 3,
    "^%#": 99
}

i = list(d.items())

i.sort()  # Sort by key, then value

# If keys are different types, force them to be the same type
# Beej doesn't yet know why this is sorting out of order, but must find out!
# i.sort(key=lambda e: str(e))

# print(i)


"""
def comp(e):
	return e[1]

i.sort(key=comp)
"""
i.sort(key=lambda e: e[1])

print(i)

# Lookup table


import math

# Build a lookup table for inverse square root for numbers 1 - 1000.

inv_sqrt_table = {}

def inv_sqrt(n):
	if n not in inv_sqrt_table:
		inv_sqrt_table[n] = 1 / math.sqrt(n)

	return inv_sqrt_table[n]

def build_lookup_table():
	for i in range(1, 10000001):
		inv_sqrt_table[i] = inv_sqrt(i)

build_lookup_table()

#print(inv_sqrt_table[10])
#print(inv_sqrt_table[37])


print(inv_sqrt(10))
print(inv_sqrt(37))
print(inv_sqrt(10000000000))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))
print(inv_sqrt(37))