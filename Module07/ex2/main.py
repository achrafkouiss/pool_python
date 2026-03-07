from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard
from enum import Enum

class Rarity(Enum):
    COMMON: str = "Common"
    UNCOMMON: str = "Uncomon"
    RARE: str = "Rare"
    ELITE: str = "Elite"
    LEGENDARY: str = "Lgendary"

print("\n=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
print("- Card: ",
       [name for name, attribute in Card.__dict__.items() if callable(attribute) and not name.startswith('__')])
print("- Combatable: ",
       [name for name, attribute in Combatable.__dict__.items() if callable(attribute) and not name.startswith('__')])
print("- Magical: ",
       [name for name, attribute in Magical.__dict__.items() if callable(attribute) and not name.startswith('__')])

print("\nPlaying Arcane Warrior (Elite Card):\n")

arcane_warrior = EliteCard("Arcane Warrior", 5, Rarity.ELITE.value, 5, "melee")
print("Combat phase:")
print("Attack result:", arcane_warrior.attack("Enemy"))
print("Defense result:", arcane_warrior.defend(2))

print("\nMagic phase:")
print("Spell cast:", arcane_warrior.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
print("Mana channel:", arcane_warrior.channel_mana(3))

print("\nMultiple interface implementation successful!")
