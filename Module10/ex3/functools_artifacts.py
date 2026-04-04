from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> Callable:
    def combine(operation: str) -> int:
        if operation == "add":
            result = reduce(add, spells)
        elif operation == "multiply":
            result = reduce(mul, spells)
        elif operation == "max":
            result = reduce(max, spells)
        elif operation == "min":
            result = reduce(min, spells)
        return result

    return combine

# def base_enchantment(target: str, power: int, element: str) -> str:
#     return f"{element} enchantment hits {target} with power {power}"


def partial_enchanter(
    base_enchantment: Callable,
) -> dict[str, Callable]:
    return {
        "fire_enchant": partial(base_enchantment, power=50, element="fire"),
        "ice_enchant": partial(base_enchantment, power=50, element="ice"),
        "lightning_enchant": partial(
            base_enchantment, power=50, element="lightning"
            ),
    }

# enchanters = partial_enchanter(base_enchantment)

# print(enchanters["fire_enchant"]("Orc"))
# print(enchanters["ice_enchant"]("Dragon"))
# print(enchanters["lightning_enchant"]("Goblin"), "\n")


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @singledispatch
    def cast(spell: object) -> str:
        return f"Unhandled type: {type(spell).__name__}"

    @cast.register(int)
    def _(power: int) -> str:
        return f"Damage spell deals {power}"

    @cast.register(str)
    def _(enchantment: str) -> str:
        return f"Enchantment : {enchantment}"

    @cast.register(list)
    def _(spells: list) -> str:
        return f"Multi-cast : {spells}"

    return cast

# caster = spell_dispatcher()

# print(caster(100))
# print(caster("Fire Aura"))
# print(caster([10, 20, 30]))
# print(caster(3.14))


def main() -> None:
    spell_powers = [10, 20, 30, 40]
    operations = ["add", "multiply", "max"]
    fibonacci_tests = [10, 15]

    try:
        print("Testing spell reducer...")
        spell = spell_reducer(spell_powers, "min")
        for op in operations:
            print(f"{op}: {spell(op)}")

        print("\nTesting memoized fibonacci...")
        for fib in fibonacci_tests:
            print(f"Fib({fib}): {memoized_fibonacci(fib)}")

    except ValueError as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
