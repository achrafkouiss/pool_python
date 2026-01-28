class Plant:
    """Class to represent plant"""
    def __init__(self, name: str, height: int, days: int):
        """Initialize name, height and age attributes"""
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        """A method to simulate the plant height growth"""
        self.height += 1

    def age(self) -> None:
        """A method to simulate the plant age growth"""
        self.days += 1

    def get_info(self) -> None:
        """A method to print the current plant status"""
        print(f"{self.name}: {self.height}cm, {self.days} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    day = 1
    growth = 0
    print(f"=== Day {day} ===")
    rose.get_info()
    while day < 7:
        rose.grow()
        rose.age()
        day += 1
        growth += 1
    print(f"=== Day {day} ===")
    rose.get_info()
    print(f"Growth this week: +{growth}")
