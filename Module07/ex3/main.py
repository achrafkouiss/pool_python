from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine

print("\n=== DataDeck Game Engine ===\n")

print("Configuring Fantasy Card Game...")
Engine = GameEngine()
aggressiveStrategy = AggressiveStrategy()
cardfactory = FantasyCardFactory()
Engine.configure_engine(cardfactory, aggressiveStrategy)

print("Simulating aggressive turn...\n\n\n\n\n\n\n")
hand = cardfactory.create_themed_deck(3)


enemy = cardfactory.create_themed_deck(3)
priority_enemy = aggressiveStrategy.prioritize_targets(list(enemy.values()))
name_of_enemy = []
for card in priority_enemy:
    stats = card.get_card_info()
    name_of_enemy.append(stats["name"])

# aggressiveStrategy.execute_turn(list(enemy.values()), name_of_enemy)
print("Turn execution:")
print(f"Strategy: {aggressiveStrategy.__class__.__name__}")
print("Actions: ", aggressiveStrategy.execute_turn(list(enemy.values()), name_of_enemy))