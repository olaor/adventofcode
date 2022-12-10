# Read instructions from input file
with open("input.txt", "r") as file:
    instructions = file.readlines()

# Initialize X register to 1
x = 1

# Loop through instructions
for instruction in instructions:
    # Parse instruction and value
    parts = instruction.strip().split(" ")
    instr = parts[0]
    val = int(parts[1])

    # Execute instruction
    if instr == "addx":
        x += val
    elif instr == "noop":
        pass

# Print value of X register after each of the 20th, 60th, 100th, 140th, 180th, and 220th cycles
for i in range(20, 240, 40):
    print(f"After {i} cycles, X = {x * i}")

