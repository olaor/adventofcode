# Parse the input program from the input file
with open('input.txt') as f:
  program = []
  for line in f:
    parts = line.strip().split()
    if len(parts) == 1:
      # Handle instructions without arguments
      instruction = parts[0]
      value = 0
    elif len(parts) == 2:
      instruction, value = parts
      value = int(value)
    else:
      raise ValueError('Invalid instruction: %s' % line.strip())
    program.append((instruction, value))

# Initialize the X register with value 1
x = 1

# Run the program
for i, (instruction, value) in enumerate(program):
  # Update the value of the X register according to the instruction
  if instruction == 'noop':
    pass
  elif instruction == 'addx':
    x += value
  else:
    raise ValueError('Invalid instruction: %s' % instruction)
  
  # Calculate the signal strength for the current cycle
  if i == 19 or (i > 19 and (i - 20) % 40 == 0):
    signal_strength = i * x
    print('Signal strength at cycle %d: %d' % (i, signal_strength))

