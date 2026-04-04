from typing import Callable


def spell_combiner(
    spell1: Callable, spell2: Callable
) -> Callable:
    def combined(target: str) -> tuple[str, str]:
        first_spell = spell1(target)
        second_spell = spell2(target)
        return (first_spell, second_spell)

    return combined


def power_amplifier(
    base_spell: Callable, multiplier: int
) -> Callable:
    def powered_spell(x: int) -> int:
        return base_spell(x) * multiplier

    return powered_spell


def conditional_caster(
    condition: Callable, spell: Callable
) -> Callable:
    def casting_spell(target: int) -> str:
        if condition(target):
            return spell()
        else:
            return "Spell fizzled"

    return casting_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast() -> list[str]:
        return [spell() for spell in spells]

    return cast


def main() -> None:
    def fireball(target: str) -> str:
        return f" Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    activate = combined("Dragon")
    print("Combined spell result: ", end="")
    print(*activate, sep=", ")

    def damage(x: int) -> int:
        return x

    print("\nTesting power amplifier...")
    original = 10
    mega_fireball = power_amplifier(damage, 3)
    Amplified = mega_fireball(original)
    print(f"Original: {original}, Amplified: {Amplified}")


if __name__ == "__main__":
    main()
