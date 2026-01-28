class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception for watering-related problems."""
    pass


def PlantError_error():
    """raising and catching PlantError exceptions."""
    try:
        a = "wilting"
        if a == "wilting":
            raise (PlantError("The tomato plant is wilting!"))
    except PlantError as e:
        print("Testing PlantError...")
        print(f"Caught PlantError: {e}\n")


def WaterError_error():
    """raising and catching WaterError exceptions."""
    try:
        water = 10
        if water < 15:
            raise (WaterError(" Not enough water in the tank!"))
    except WaterError as e:
        print("Testing PlantError...")
        print(f"Caught PlantError: {e}\n")
    print("Testing catching all garden errors...")


def GardenError_error():
    """raising and catching GardenError exceptions."""
    try:
        water = 10
        if water < 15:
            raise (WaterError(" Not enough water in the tank!"))
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        a = "wilting"
        if a == "wilting":
            raise (PlantError("The tomato plant is wilting!"))
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")


def test_custom_error():
    """Test custom garden exceptions."""
    print("=== Custom Garden Errors Demo ===\n")
    PlantError_error()
    WaterError_error()
    GardenError_error()
    print("All custom error types work correctly!")


test_custom_error()
