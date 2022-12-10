# initialize the X register to 1
x = 1

# initialize a list to keep track of the signal strength
signal_strengths = []

# read in the program
program = [line.strip() for line in open('program.txt')]

# keep track of the current cycle
cycle = 1

# iterate over the instructions in the program
for instruction in program:
  # if the instruction is "noop", increment the cycle by 1
  if instruction == "noop":
    cycle += 1
  # otherwise, the instruction is "addx V"
  else:
    # extract the value of V from the instruction
    v = int(instruction[4:])
    # increment the X register by V
    x += v
    # increment the cycle by 2 (since the "addx" instruction takes two cycles to complete)
    cycle += 2
    # if the current cycle is a multiple of 20, add the current signal strength to the list of signal strengths
    if cycle % 20 == 0:
      signal_strengths.append(cycle * x)

# print the signal strengths during the 20th, 60th, 100th, 140th, 180th, and 220th cycles
print(sum(signal_strengths))

