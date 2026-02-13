import sys

print("=== Command Quest ===")
count_args = len(sys.argv)
if count_args == 1:
    print("No arguments provided!")
    print(f"Program name: {sys.argv[0]}")
    print("Total arguments: 1")
elif count_args > 1:
    print(f"Program name: {sys.argv[0]}")
    print(f"Arguments received: {count_args - 1}")
    index = 1
    for arg in sys.argv[1:]:
        print(f"Argument {index}: {arg}")
        index += 1
    print(f"Total arguments: {count_args}")
