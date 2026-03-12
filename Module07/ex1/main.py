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

Lightning_bolt = SpellCard("Lightning Bolt", 3, Rarity.COMMON.value, "buff")
mana_crystal = ArtifactCard(
    "Mana Crystal", 2, Rarity.COMMON.value, 5, "Permanent: +1 mana per turn"
)
fire_dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)

deck = Deck()
deck.add_card(Lightning_bolt)
deck.add_card(mana_crystal)
deck.add_card(fire_dragon)


print("\nBuilding deck with different card types...")
print(f"Deck stats: {deck.get_deck_stats()}\n")

print("Drawing and playing cards:\n")
for _ in deck.list_of_cards[:]:
    card = deck.draw_card()
    if isinstance(card, CreatureCard):
        card_type = "Creature"
    elif isinstance(card, SpellCard):
        card_type = "Spell"
    elif isinstance(card, ArtifactCard):
        card_type = "Artifact"
    print(f"Drew: {card.name} ({card_type})")
    print(f"Play result: {card.play({'mana': 6})}\n")

print("Polymorphism in action: Same interface, different card behaviors!")
