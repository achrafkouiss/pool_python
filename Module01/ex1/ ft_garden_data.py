class Plant:
    """Class to represent plant"""
    def __init__(self, name, height, age):
        """Initialize name, height and age attributes"""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    lst = [
            Plant("Rose", 25, 30),
            Plant("Sunflower", 80, 45),
            Plant("Cactus", 125, 120),
            ]
    i = 0
    while i < 3:
        print(f"{lst[i].name}: {lst[i].height}cm, {lst[i].age} days old")
        i += 1
