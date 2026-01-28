class Plant:
    """ base Plant that has common features (name, height, age)"""
    def __init__(self, name, height, age):
        """Initialize name, height and age attributes"""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """childclass to Plant that represent flower and it inherite(name,
     height, age) and has new features wich is color and a new methode bloom"""
    def __init__(self, name, height, age, color):
        """Initialize name, height, age and color attributes the first
        3 are inherited"""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Print a message indicating that the flower is blooming."""
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """childclass to Plant that represent Tree and it inherite (name,
        height, age) and has new features wich is trunk_diameter and a new
        methode produce_shade"""
    def __init__(self, name, height, age, trunk_diameter):
        """Initialize name, height, age and trunk_diameter attributes
        the first 3 are inherited"""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        """
        Calculate and print the shade area produced by the tree.
        The shade area is roughly estimated using height and trunk diameter.
        """
        shade_area = 31.2 * (self.height / 100) * (self.trunk_diameter / 100)
        print(f"{self.name} provides {int(shade_area)} square meters of shade")


class Vegetable(Plant):
    """childclass to Plant that represent Vegetable and it inherite (name,
    height, age) and has new features wich are harvest_season and
    nutritional_value"""
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        """Initialize name, height, age, harvest_season and nutritional_value
          attributes the first 3 are inherited"""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")
    rose = Flower("Rose", 25, 30, "red")
    Sunflower = Flower("Sunflower", 30, 35, "yellow")
    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, ", end="")
    print(f"{rose.color} color")
    rose.bloom()
    print("")
    Oak = Tree("Oak", 500, 1825, 50)
    palm = Tree("palm", 600, 2000, 100)
    print(f"{Oak.name} (Tree): {Oak.height}cm, {Oak.age} days, ", end="")
    print(f"{Oak.trunk_diameter} diameter")
    Oak.produce_shade()
    print("")
    tomato = Vegetable("tomato", 80, 90, "summer", "C")
    potato = Vegetable("potato", 600, 2000, "winter", "D")
    print(f"{tomato.name} (Vegetable): {tomato.height}cm, ", end="")
    print(f"{tomato.age} days, {tomato.harvest_season} harvest")
    print(f"{tomato.name} is rich in vitamin {tomato.nutritional_value}")
