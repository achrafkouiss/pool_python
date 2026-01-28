def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def ft_print_days(days):
        if days > 1:
            ft_print_days(days - 1)
        print(f"Days : {days}")
    ft_print_days(days)
    print("Harvest time!")
