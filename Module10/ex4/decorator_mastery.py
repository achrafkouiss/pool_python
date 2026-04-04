import time
from functools import wraps
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"{func.__name__} took {end_time - start_time:.4f}s")
        return result
    return wrapper


def power_validator(
    min_power: int,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_power = kwargs.get("power")
            if current_power is None and len(args) > 2:
                current_power = args[2]

            if current_power is not None and current_power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1} failed: {e}")

            print(f"All {max_attempts} attempts failed.")
            return None
        return wrapper

    return decorator

# import random

# @retry_spell(3)
# def unstable_spell() -> str:
#     if random.random() < 0.7:
#         raise ValueError("Spell fizzled!")
#     return "Spell succeeded!"


# print("\nTesting retry_spell...")
# result = unstable_spell()
# print(f"Final result: {result}")

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 3 and all(c.isalpha() or c.isspace() for c in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")
    print()

    print("Testing MageGuild...")
    guild = MageGuild()
    print(f"{guild.validate_mage_name('achraf kouiss')}")
    print(f"{guild.validate_mage_name('achraf15')}")

    print(f"{guild.cast_spell('Lightning', 15)}")
    print(f"{guild.cast_spell('Healing', 5)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
