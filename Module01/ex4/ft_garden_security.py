class SecurePlant:
    """
    Class to represent plant and make in sure they
    are protected and encapsulated
    """
    def __init__(self, name):
        """Initialize name, height and age attributes"""
        self.name = name
        self._height = 0
        self._age = 0

    def set_height(self, height):
        """
        modify plant height after checking that it is
        not negative and print if it's updated or not
        """
        if height > 0:
            self._height = height
            print(f"Height updated: {height}cm [OK]")
        else:
            print(f"Invalid operation attempted: height {height}cm [REJECTED]")
            print("Security: Negative height rejected")

    def set_age(self, age):
        """
        modify plant age after checking that it is
        not negative and print if it's updated or not
        """
        if age > 0:
            self._age = age
            print(f"Age updated: {age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age} days [REJECTED]")
            print("Security: Negative age rejected")

    def get_height(self):
        """return the height of the plant"""
        return self._height

    def get_age(self):
        """return the age of the plant"""
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose")
    print(f"Plant created: {rose.name}")
    rose.set_height(25)
    rose.set_age(30)
    print("")
    rose.set_height(-5)
    print("")
    print(f"Current plant: {rose.name} ({rose.get_height()}cm", end="")
    print(f", {rose.get_age()} days")
