from ex1.Deck import Deck
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex0.CreatureCard import CreatureCard
from enum import Enum

class Rarity(Enum):
    COMMON: str = "Common"
    UNCOMMON: str = "Uncomon"
    RARE: str = "Rare"
    ELITE: str = "Elite"
    LEGENDARY: str = "Lgendary"

print("\n=== DataDeck Deck Builder ===\n")

Lightning_bolt = SpellCard("Lightning Bolt", 3, Rarity.COMMON.value,"buff")
mana_crystal = ArtifactCard("Mana Crystal", 2, Rarity.COMMON.value, 5,
                         "Permanent: +1 mana per turn")
fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)

deck = Deck()
deck.add_card(Lightning_bolt)
deck.add_card(mana_crystal)
deck.add_card(fire_dragon)


print("\nBuilding deck with different card types...")
print(f"Deck stats: {deck.get_deck_stats()}\n")

print("Drawing and playing cards:\n")
#looping thraugh a copy because when we loop over the list the we face a probleme the list index go but the list is shortened in this case it loop only 2 times not 3 
for _ in deck.list_of_cards[:]:
    card = deck.draw_card()
    if type(card).__name__ == "CreatureCard":
        card_type = "Creature"
    elif type(card).__name__ == "SpellCard":
        card_type = "Spell"
    elif type(card).__name__ == "ArtifactCard":
        card_type = "Artifact"
    print(f"Drew: {card.name} ({card_type})")
    print(f"Play result: {card.play({'mana': 6})}\n")

print("Polymorphism in action: Same interface, different card behaviors!")