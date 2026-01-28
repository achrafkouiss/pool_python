def garden_operations():
    """Demonstrate different built-in Python exceptions and
    how to catch them"""
    try:
        a = int("ach")
        print(a)
    except ValueError:
        print("Testing ValueError...")
        print("Caught ValueError: invalid literal for int()\n")
    try:
        b = 10 / 0
        print(b)
    except ZeroDivisionError:
        print("Testing ZeroDivisionError...")
        print("Caught ZeroDivisionError: division by zero\n")
    try:
        file = "missing.text"
        open(file, "r")
    except FileNotFoundError:
        print("Testing ZeroDivisionError...")
        print(f"Caught FileNotFoundError: No such file '{file}'\n")
    try:
        d = {
            'name': 'achraf',
            'age': 25
        }
        d['missing\\_plant']
    except KeyError:
        print("Testing KeyError...")
        print("Caught KeyError: 'missing\\_plant'\n")
    try:
        a = int("ach")
    except (ValueError, ZeroDivisionError):
        print("Testing multiple errors together...")
        print("Caught an error, but program continues!\n")


def test_error_types():
    """Run all error demonstrations and confirm program continues safely."""
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


test_error_types()
