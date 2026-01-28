def water_plants(plant_list):
    """Water plants and always close the system using a finally block."""
    print("Opening watering system")
    try:
        for plant in plant_list:
            plant + ""
            print(f"Watering {plant}")
    except Exception:
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Test normal and failing watering scenarios with guaranteed cleanup."""
    plant_list1 = ["tomato", "lettuce", "carrots"]
    plant_list2 = ["tomato", None]
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(plant_list1)
    print("Watering completed successfully!")
    print("\nTesting with error...")
    water_plants(plant_list2)
    print("\nCleanup always happens, even with errors!")


test_watering_system()
