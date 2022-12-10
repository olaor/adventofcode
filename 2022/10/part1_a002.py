# define a function to execute a single instruction
def execute_instruction(x, instruction):
  # split the instruction into its parts
  parts = instruction.split()
  
  # if the instruction is "noop", do nothing
  if parts[0] == "noop":
    return x
  
  # if the instruction is "addx", add the specified value to the register
  elif parts[0] == "addx":
    return x + int(parts[1])
  
  # if the instruction is not recognized, raise an error
  else:
    raise ValueError("Unrecognized instruction: " + instruction)

# define the main function
def main(program):
  # initialize the register with a value of 1
  x = 1
  
  # initialize a list to store the signal strengths
  signal_strengths = []
  
  # execute the program
  for i in range(1, len(program) + 1):
    # execute the instruction
    x = execute_instruction(x, program[i-1])
    
    # if the current cycle is a multiple of 20 or 40, store the signal strength
    if i % 20 == 0 or i % 40 == 0:
      signal_strengths.append(x * i)
  
  # return the list of signal strengths
  return signal_strengths

# define the program
program = [
  "noop",
  "addx 3",
  "addx -5"
]

# execute the program and print the result
print(main(program))
