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
            Plant("Oak", 200, 365),
            Plant("Cactus", 5, 90),
            Plant("Sunflower", 80, 45),
            Plant("Fern", 15, 120),
            ]
    print("=== Plant Factory Output ===")
    i = 0
    while i < 5:
        print(f"created: {lst[i].name} ({lst[i].height}cm, {lst[i].age} days)")
        i += 1
    print("")
    print(f"Total plants created: {i}")
