import sys
import math

print("=== Game Coordinate System ===\n")

try:
    new_tuple1 = (10, 20, 5)
    x, y, z = new_tuple1
    distance = math.sqrt((0-x)**2 + (0-y)**2 + (0-z)**2)
    print("Parsed position: ", {new_tuple1})
    print(f"Distance between (0, 0, 0) and {new_tuple1}: {distance:.2f}\n")
except Exception as e:
    print("Error in demo tuple 1:", e.__class__.__name__, e)

try:
    new_tuple2 = (3, 4, 0)
    x, y, z = new_tuple2
    distance = math.sqrt((0-x)**2 + (0-y)**2 + (0-z)**2)
    print("Parsing coordinates: \"3,4,0\"")
    print("Parsed position: ", {new_tuple2})
    print(f"Distance between (0, 0, 0) and {new_tuple2}: {distance:.2f}\n")
except Exception as e:
    print("Error in demo tuple 2:", e.__class__.__name__, e)

args_lenght = len(sys.argv)
all_nums = []

if 1 < args_lenght <= 3:
    try:
        i = 1

        while i < len(sys.argv):
            if "," in sys.argv[i]:
                nums = sys.argv[i].split(",")
            else:
                nums = sys.argv[i].split()
            nums_lenght = len(nums)
            if nums_lenght < 3:
                raise ValueError("not enough coordinates")
            elif nums_lenght > 3:
                raise ValueError("too much coordinates")
            for num in nums:
                all_nums += [int(num)]
            i += 1

    except ValueError as e:
        msg, = e.args

        print("Parsing invalid coordinates: \"", end="")
        index = 0
        for num in nums:
            if index != nums_lenght - 1:
                print(f"{num},", end="")
            else:
                print(f"{num}\"")
            index += 1
        print("Error parsing coordinates: ", {msg})
        print(f"Error details - Type: {e.__class__.__name__}, " +
              f"Args: (\"{msg}\",)")
        all_nums = []
    except Exception as e:
        print("Unexpected error while parsing coordinates:",
              e.__class__.__name__, e)
        all_nums = []

lenght = len(all_nums)

if lenght == 3:
    try:
        new_tuple3 = tuple(all_nums)
        x, y, z = new_tuple3
        distance = math.sqrt((0-x)**2 + (0-y)**2 + (0-z)**2)
        print("Parsed position: ", {new_tuple3})
        print(f"Distance between (0, 0, 0) and {new_tuple3}: {distance:.2f}")
        print("\nUnpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print("PlayCoordinateser: X=0, Y=0, Z=0")
    except Exception as e:
        print("Unexpected error in 3-value block:", e.__class__.__name__, e)

elif lenght == 6:
    try:
        first_coordinates = tuple(all_nums[0:3])
        second_coordinates = tuple(all_nums[3:6])
        x1, y1, z1 = first_coordinates
        x2, y2, z2 = second_coordinates
        distance = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
        print("Parsed position:", {first_coordinates}, {second_coordinates})
        print(f"Distance between {first_coordinates}" +
              f" and {second_coordinates}: {distance:.2f}")

        print("\nUnpacking demonstration:")
        print(f"Player at x={x1}, y={y1}, z={z1}")
        print(f"PlayCoordinateser: X={x2}, Y={y2}, Z={z2}")
    except Exception as e:
        print("Unexpected error in 6-value block:", e.__class__.__name__, e)

try:
    print("\nUnpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print("PlayCoordinateser: X=0, Y=0, Z=0")
except Exception as e:
    print("\nUnexpected error in final print:", e.__class__.__name__, e)
