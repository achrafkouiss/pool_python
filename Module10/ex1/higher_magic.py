def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(target):
        first_spell = spell1(target)
        second_spell = spell2(target)
        return (first_spell, second_spell)
    return combined


def fireball(target):
    return f" Fireball hits {target}"


def heal(target):
    return f"Heals {target}"


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def powered_spell(x):
        return base_spell(x) * multiplier
    return powered_spell

def damage(x):
    return x

def conditional_caster(condition: callable, spell: callable) -> callable:
    def casting_spell(target):
        if condition(target):
            return spell()
        else:
            return "Spell fizzled"
    return casting_spell

def lightning():
    return "lightning attack"

def mana_reserve(mana):
    if mana > 0:
        return True
    else:
        return False
    

def spell_sequence(spells: list[callable]) -> callable:
    def cast():
        return [spell() for spell in spells]
    return(cast)

def move_earth():
    return "Earth moved"

def necromancy():
    return "Summoning Undead"

def tornado():
    return "summoning Tornado"


def main():
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    activate = combined("Dragon")
    print("Combined spell result: ", end="")
    print(*activate, sep=", ")

    print("\nTesting power amplifier...")
    original = 10
    mega_fireball = power_amplifier(damage, 3)
    Amplified = mega_fireball(original)
    print(f"Original: {original}, Amplified: {Amplified}")
    

if __name__ == "__main__":
    main()