# read instructions from input.txt file
with open("input.txt", "r") as input_file:
    instructions = input_file.readlines()

# initialize X register with value 1
x = 1

# iterate over instructions
for instruction in instructions:
    # split instruction into command and value
    parts = instruction.split(" ")
    if len(parts) == 2:
        command, value = parts
    else:
        command = "noop"
        value = None
    
    # execute command
    if command == "addx":
        x += int(value)
    elif command == "noop":
        pass

# print final value of X register
print(x)
