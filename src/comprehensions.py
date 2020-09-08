# say we want to store all of the even numbers in the range
# 0-100 in a list
# what are some ways we can do this?
evens = []

# # loop through the range
for i in range(101):
    if i % 2 == 0:
        evens.append(i)

print(evens)

# # comprehensions allow us to write the above logic in a much
# # more terse fashion
# evens_2 = [i for i in range(101) if i % 2 == 0]
# # print(evens)
# print(evens_1 == evens_2)

# create a list of the square values of numbers in the range 1-10

# squares_1 = []
odds = [n for n in range(101) if n % 2 == 1]

print(f"odds: {odds}")

squares = [x * x for x in range(1, 11)]

print(f"squares: {squares}")

names = ["Sarah", "jorge", "sam", "Jake", "jeremy", "sandy", "shawn"]

# create a new list containing only the names that start with `s`
# and also make sure all of the names are properly capitalized
s_names = []
j_names = []

for name in names:
    if name[0].lower() == 's':
        s_names.append(name.capitalize())
# if it does, add it to `s_names`, making sure the
# name is properly capitalized
print(s_names)
# print(names)

j_names = [name.capitalize() for name in names if name[0].lower() == 'j']

print(j_names)

# comprehensions work just as well with dicts as well
string = "abcdefghijklmnopqrstuvwxyz"

alpha = {letter: i + 1 for i, letter in enumerate(string)}

# for i, letter in enumerate(string):
#     alpha[letter] = i + 1

print(f"{string} alpha: {alpha}")
