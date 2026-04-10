import sys

args = sys.argv
print("=== Command Quest ===")
print("Program name:  ", args[0])
if len(args) == 1:
    print("No arguments provided!")
else:
    print("Arguments  received:  ", len(args) - 1)
    for i in range(1, len(args)):
        print(f"Argument {i}:  {args[i]}")
print("Total arguments:  ", len(args))
