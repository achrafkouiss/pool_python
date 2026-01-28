def ft_water_reminder():
    Days = int(input("Days since last watering:  "))
    if Days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
