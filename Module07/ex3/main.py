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

hand = cardfactory.create_themed_deck(3)
print("\nSimulating aggressive turn...")
turn = Engine.simulate_turn()
turn_len = len(turn)
index: int = 0
print("hand: [", end="")
for key, value in turn.items():
    if index < turn_len - 1:
        print(f"{key} ({value}), ", end="")
    else:
        print(f"{key} ({value})]\n")
    index += 1

enemy = cardfactory.create_themed_deck(3)
priority_enemy = aggressiveStrategy.prioritize_targets(list(enemy.values()))
name_of_enemy = []
for card in priority_enemy:
    stats = card.get_card_info()
    name_of_enemy.append(stats["name"])

# aggressiveStrategy.execute_turn(list(enemy.values()), name_of_enemy)
print("Turn execution:")
print(f"Strategy: {aggressiveStrategy.__class__.__name__}")
print(f"Actions: {aggressiveStrategy.execute_turn(list(enemy.values()), name_of_enemy)}\n")

print("Game Report:")
print(f"{Engine.get_engine_status()}\n")

print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
