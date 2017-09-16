from sys import argv

def get_input():
  filename = argv[1]
  with open(filename, "r") as f:
    text = f.read()
  return text

def write_output(output):
  filename = argv[1]
  with open(filename + ".out", "w") as f:
    f.write(output)



response = get_input()

# Your code here

output = "0" if "dream" in response else "1"

# output should be equal to "0" if you want to let the user continue to checkout,
# and some integer greater than zero otherwise
write_output(output)
