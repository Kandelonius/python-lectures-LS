empty = []

nums = [10, 60, 20, 5]

print(nums)

nums.append(77)
print(nums)

for elem in nums:
    print(elem)

for n in range(10):
    print(n)

print("\n")

for n in range(2, 10):
    print(n)

for i in range(len(nums)):
    print(i)

for i in range(len(nums)):
    print(i, nums[i])

for i, v in enumerate(nums):
    print(i, v)
