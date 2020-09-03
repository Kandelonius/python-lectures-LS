# In Python, arrays are called "lists"

# create an empty list
empty = []

# create a list with some numbers
nums = [10, 60, 20, 5]
print(nums)
# print out our list of numbers
# print(nums)

# add a number to our `nums` list

nums.append(77)
print(nums)

# let's print out every value in the `nums` list
# one at a time
for elem in nums:
    print(elem)

for n in range(10):
    print(n)

print("\n")

# what if we want to iterate x number of times?
for n in range(2, 10):
    print(n)

# what if we want to iterate along the length of a list?
for i in range(len(nums)):
    print(i)

for i in range(len(nums)):
    print(i, nums[i])

# another way to print out elements from a list with their
# associated index
for i, v in enumerate(nums):
    print(i, v)
