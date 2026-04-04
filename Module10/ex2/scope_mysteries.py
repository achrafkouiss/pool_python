from typing import Callable


def mage_counter() -> Callable:
    counter = 0

    def called_count() -> int:
        nonlocal counter
        counter += 1
        return counter

    return called_count


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def accumulated_power(added_power: int) -> int:
        nonlocal power
        power += added_power
        return power

    return accumulated_power

# print("Testing spell accumulator...")
# acc = spell_accumulator(100)

# print(acc(10))   # 110
# print(acc(20))   # 130
# print(acc(-50))  # 80
# print()


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchanted_name(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchanted_name


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, object] = {}

    def store(key: str, value: object) -> None:
        memory[key] = value

    def recall(key: str) -> object:
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}

# print("Testing memory vault...")
# vault = memory_vault()

# vault["store"]("spell", "Fireball")
# vault["store"]("power", 999)

# print(vault["recall"]("spell"))
# print(vault["recall"]("power"))
# print(vault["recall"]("unknown"))


def main() -> None:
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}\n")

    print("Testing enchantment factory...")
    enchantment_types = {"Flaming": "Sword", "Frozen": "Shield"}
    for key, val in enchantment_types.items():
        print(enchantment_factory(key)(val))


if __name__ == "__main__":
    main()
