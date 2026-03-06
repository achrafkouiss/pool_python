from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard

print("\n=== DataDeck Ability System ===\n")

print("EliteCard capabilities:")
print("- Card: ",
       [name for name, attribute in Card.__dict__.items() if callable(attribute) and not name.startswith('__')])
print("- Combatable: ",
       [name for name, attribute in Combatable.__dict__.items() if callable(attribute) and not name.startswith('__')])
print("- Magical: ",
       [name for name, attribute in Magical.__dict__.items() if callable(attribute) and not name.startswith('__')])

print("\nPlaying Arcane Warrior (Elite Card):\n")

arcane_warrior = EliteCard("Arcane Warrior", 5, "Elite")
enemy = EliteCard("Enemy", 3, "common")
print("Combat phase:")
print(f"Attack result: {arcane_warrior.attack(enemy)}")
