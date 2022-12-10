# read instructions from input.txt file
with open("input.txt", "r") as input_file:
    instructions = input_file.readlines()

# initialize X register with value 1
x = 1

# iterate over instructions
for instruction in instructions:
    # split instruction into command and value
    command, value = instruction.split()
    
    # execute command
    if command == "addx":
        x += int(value)
    elif command == "noop":
        pass

# print final value of X register
print(x)

