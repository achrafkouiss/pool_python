def check_plant_health(plant_name, water_level, sunlight_hours):
    """Validate plant parameters and raise errors when values are invalid."""
    try:
        if plant_name == "":
            print("Testing empty plant name...")
            raise (ValueError("Plant name cannot be empty!"))
        elif water_level > 10:
            print("Testing bad water level...")
            raise (ValueError(f"Water level {water_level} "
                              + "is too high (max 10)"))
        elif water_level < 1:
            print("Testing bad water level...")
            raise (ValueError(f"Water level {water_level} is too low (min 0)"))
        elif sunlight_hours > 12:
            print("Testing bad sunlight hours...")
            raise (ValueError(f"Sunlight hours {sunlight_hours} "
                              + "is too high (max 12)"))
        elif sunlight_hours < 2:
            print("Testing bad sunlight hours...")
            raise (ValueError(f"Sunlight hours {sunlight_hours} "
                              + "is too low (min 2)"))
        print("Testing good values...")
        print(f"Plant '{plant_name}' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")


def test_plant_checks():
    """Run health checks with valid and invalid plant data."""
    print("=== Garden Plant Health Checker ===\n")
    check_plant_health("tomato", 5, 10)
    print()
    check_plant_health("", 5, 10)
    print()
    check_plant_health("tomato", 15, 10)
    print()
    check_plant_health("tomato", 5, 0)
    print("\nAll error raising tests completed!")


test_plant_checks()
