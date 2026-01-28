class GardenError(Exception):
    """Base exception for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Exception for plant-related problems."""
    pass


class WaterError(GardenError):
    """Exception for watering-related problems."""
    pass


class GardenManager:
    """Manage plants, watering operations, and health monitoring."""
    plants = []

    def add_plants(self, plant):
        """Add a new plant to the garden with default values."""
        try:
            if plant == "":
                raise (PlantError("Plant name cannot be empty!"))
            elif plant.__class__.__name__ != "str":
                raise (PlantError("Plant name should be a string"))
            self.plants = self.plants + [{
                "plant_name": plant,
                "water_level": 0,
                "sunlight_hours": 8,
            }]
            print(f"Added {plant} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")

    def water_plants(self):
        """Water all plants and always close the watering system safely."""
        try:
            print("Opening watering system")
            if not self.plants:
                raise (WaterError("No plant to water"))
            for dictionary in self.plants:
                dictionary['water_level'] += 5
                print(f"Watering {dictionary['plant_name']} - success")
        except (WaterError, KeyError, ValueError) as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)\n")

    def check_plant_health(self):
        """Check plant status and raise errors when limits are exceeded."""
        tank = 0
        try:
            print("Checking plant health...")
            for dictionary in self.plants:
                if dictionary['water_level'] > 10:
                    raise (WaterError(f"Water lvl {dictionary['water_level']}"
                                      + " is too high (max 10)"))
                elif dictionary['water_level'] < 0:
                    raise (WaterError(f"Water lvl {dictionary['water_level']}"
                                      + "is too low (min 0)"))
                elif dictionary['sunlight_hours'] > 12:
                    raise (PlantError("Sunlight hours "
                                      + dictionary['sunlight_hours']
                                      + " is too high (max 12)"))
                elif dictionary['sunlight_hours'] < 0:
                    raise (PlantError("Sunlight hours "
                                      + dictionary['sunlight_hours']
                                      + " is too low (min 2)"))
                print(f"{dictionary['plant_name']}: healthy (water: "
                      + f"{dictionary['water_level']}, sun: "
                      + f"{dictionary['sunlight_hours']})")
        except GardenError as e:
            try:
                print(f"Error checking {dictionary['plant_name']}: {e}")
            except KeyError as e:
                print(f"Caught KeyError: {e}\n")
        except KeyError as e:
            print(e)
        if tank == 0:
            raise (WaterError("Not enough water in tank"))


def test_garden_management():
    """Full test of the garden management system and error recovery."""
    park = GardenManager()
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    park.add_plants("tomato")
    park.add_plants("lettuce")
    park.add_plants("")
    print("\nWatering plants...")
    park.plants[1]['water_level'] += 10
    park.water_plants()
    try:
        park.check_plant_health()
    except GardenError as e:
        print("\nTesting error recovery...")
        print(f"Caught GardenError: {e}")
    print("System recovered and continuing...\n")
    print("Garden management system test complete!")


test_garden_management()
