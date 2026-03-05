from .CreatureCard import CreatureCard
try:
    print("\n=== DataDeck Card Foundation ===\n")

    print("\nTesting Abstract Base Class Design:\n")

    print("CreatureCard Info:")
    obj = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    card_info = obj.get_card_info()
    print(card_info, "\n")

    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {obj.is_playable(6)}")
    print(f"Play result: {obj.play({'mana': 4})}\n")

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: ")
except ValueError:
    pass