print("Hello world!")

name = "Shane"

print(f"Hello {name}")

print(f'Someone\'s name is {name}')

# how do we print "Hello world" in Python?
print("Hello world")

# How does this differ from how you would do it in your
    # core track language?
# JS: console.log("Hello world")

# How does how we ran this program differ from how we'd do
# it in your core track language?
# iOS: compile the swift file with Xcode, and then run the binary
# JS: 1. run it in the browser
#     2. node [filename.js]
# Java: 1. compile using the java compiler into a jar file
#       2. execute the jar file

name = "Bob"

# String interpolation using `+`
# print("Hello " + name)

# String interpolation using f-strings
# print(f'Hello {name}')

# if statements
# in Python, whitespace is important
if name != "Sean":
    print("Hey, you aren't Sean")
else:
    print(f"Hello {name}")