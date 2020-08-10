
command = ['n', 's', 'w', 'e']

selection = input()

if selection in command:
    print(selection)

#Constant time
command[3]  # the size doesn't affect the efficiency of the operation

#linear time
for command in command: # the size of the input has a direct impact on the efficiency
    print(command)

# Constant < Linear

# What's being compared is how quickly the efficiency grows as a result of the input size
