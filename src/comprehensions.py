evens = []

for i in range(101):
    if i % 2 == 0:
        evens.append(i)

print(evens)

odds = [n for n in range(101) if n % 2 == 1]

print(f"odds: {odds}")

squares = [x * x for x in range(1, 11)]

print(f"squares: {squares}")

names = ["Sarah", "jorge", "sam", "Jake", "jeremy", "sandy", "shawn"]

s_names = []
j_names = []

for name in names:
    if name[0].lower() == 's':
        s_names.append(name.capitalize())

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
