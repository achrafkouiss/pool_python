def check_temperature(temp_str):
    """Validate a temperature string and ensure it is between 0 and 40."""
    try:
        print(f"Testing temperature: {temp_str}")
        tmp = int(temp_str)
        if tmp < 0:
            print(f"Error: {tmp}°C is too cold for plants (min 0°C)")
        elif tmp > 40:
            print(f"Error: {tmp}°C is too hot for plants (max 40°C)")
        else:
            print(f"Temperature {tmp}°C is perfect for plants!")
            return tmp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    """Run several temperature tests and show safe error handling."""
    print("=== Garden Temperature Checker ===\n")
    check_temperature("25")
    print()
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")
    print()
    print("All tests completed - program didn't crash!")


test_temperature_input()
