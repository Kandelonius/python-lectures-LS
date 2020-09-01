d = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}
num = 0

for key in d:
    if (type(d[key]) == int):
        num += d[key]

print(num)