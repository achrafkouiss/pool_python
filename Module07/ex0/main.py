from .CreatureCard import CreatureCard
from enum import Enum

class Rarity(Enum):
    COMMON: str = "Common" 
    UNCOMMON: str = "Uncomon"
    RARE: str = "Rare"
    ELITE: str = "Elite"
    LEGENDARY: str = "Lgendary"


print("\n=== DataDeck Card Foundation ===\n")

print("\nTesting Abstract Base Class Design:\n")

print("CreatureCard Info:")
fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
goblin_warrior = CreatureCard("Goblin Warrior", 2, Rarity.COMMON.value, 2, 10)
fire_dragon_card_info = fire_dragon.get_card_info()
print()
print(fire_dragon_card_info, "\n")

print("Playing Fire Dragon with 6 mana available:")
print(f"Playable: {fire_dragon.is_playable(6)}")
print(f"Play result: {fire_dragon.play({'mana': 6})}\n")


print("Fire Dragon attacks Goblin Warrior:")
print(
    f"Attack result: {fire_dragon.attack_target(goblin_warrior)}\n"
    )
print("Testing insufficient mana (3 available):")
print(f"Playable: {fire_dragon.is_playable(3)}\n")

print("Abstract pattern successfully demonstrated!")

