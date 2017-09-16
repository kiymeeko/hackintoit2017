from sys import argv
from predict import main

def get_input():
  filename = argv[1]
  with open(filename, "r") as f:
    text = f.readlines()
  return text

def write_output(output):
  filename = argv[1]
  with open(filename + ".out", "w") as f:
    f.write(output)


lines = argv[1]
# Your code here
filename = argv[1]
output = main(filename)

# output should be equal to "0" if you want to let the user continue to checkout,
# and some integer greater than zero otherwise
write_output(str(output))
