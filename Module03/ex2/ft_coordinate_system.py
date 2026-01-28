import sys
import math

print("=== Game Coordinate System ===\n")

new_tuple1 = (10, 20, 5)
x, y, z = new_tuple1
distance = math.sqrt((0-x)**2 + (0-y)**2 + (0-z)**2)
print(f"Parsed position: {new_tuple1}")
print(f"Distance between (0, 0, 0) and {new_tuple1}: {distance:.2f}\n")

new_tuple2 = (3, 4, 0)
x, y, z = new_tuple2
distance = math.sqrt((0-x)**2 + (0-y)**2 + (0-z)**2)
print("Parsing coordinates: \"3,4,0\"")
print(f"Parsed position: {new_tuple2}")
print(f"Distance between (0, 0, 0) and {new_tuple2}: {distance:.2f}\n")


args = sys.argv[1:]
all_numbers = []

for arg in args:
    try:
        all_numbers += [int(arg)]
    except (ValueError, OverflowError):
        try:
            parts = arg.split()
            print(f"Position created: \"", end="")
            for part in parts:
                if part != parts[-1]:
                    print(f"{part},", end="")
                else:
                    print(f"{part}\"")
            for num in arg.split():
                all_numbers += [int(num)]
        except (ValueError, OverflowError) as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {e.__class__.__name__}, Args: (\"{e}\",)")



if len(all_numbers) == 3:
    new_tuple3 = tuple(all_numbers)
    x, y, z = new_tuple3
    distance = math.sqrt((0-x)**2 + (0-y)**2 + (0-z)**2)
    print(f"Parsed position: {new_tuple3}")
    print(f"Distance between (0, 0, 0) and {new_tuple3}: {distance:.2f}")

print("\nUnpacking demonstration:")
print(f"Player at x={x}, y={y}, z={z}")
print(f"PlayCoordinateser: X={x}, Y={y}, Z={z}")