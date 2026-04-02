def mage_counter() -> callable:
    counter = 0
    def called_count():
        nonlocal counter
        counter += 1
        return counter
    return called_count



def spell_accumulator(initial_power: int) -> callable:
    power = initial_power
    def accumulated_power(added_power):
        nonlocal power
        power += added_power
        return power
    return accumulated_power


def enchantment_factory(enchantment_type: str) -> callable:

    def enchanted_name(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanted_name


def memory_vault() -> dict[str, callable]:
    memory = {}

    def store(key, value):
        memory[key] = value
        print(memory)

    def recall(key):
        print(memory)
        return memory.get(key, "Memory not found")
 
    return {"store": store, "recall": recall}


def main():
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}\n")

    print("Testing enchantment factory...")
    enchantment_types = {
        "Flaming": "Sword",
        "Frozen": "Shield"
    }
    for key, val in enchantment_types.items():
        print(enchantment_factory(key)(val))


if __name__ == "__main__":
    main()