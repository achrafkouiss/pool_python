from typing import Dict, List
from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine

print("\n=== DataDeck Game Engine ===\n")

print("Configuring Fantasy Card Game...")

Engine: GameEngine = GameEngine()
aggressiveStrategy: AggressiveStrategy = AggressiveStrategy()
cardfactory: FantasyCardFactory = FantasyCardFactory()

Engine.configure_engine(cardfactory, aggressiveStrategy)

hand: Dict[int, object] = cardfactory.create_themed_deck(3)

print("\nSimulating aggressive turn...")

turn: Dict[str, int] = Engine.simulate_turn()
turn_len: int = len(turn)

index: int = 0

print("hand: [", end="")

for key, value in turn.items():
    if index < turn_len - 1:
        print(f"{key} ({value}), ", end="")
    else:
        print(f"{key} ({value})]\n")

    index += 1

enemy: Dict[int, object] = cardfactory.create_themed_deck(3)

priority_enemy: List[object] = aggressiveStrategy.prioritize_targets(
    list(enemy.values())
)

name_of_enemy: List[str] = []

for card in priority_enemy:
    stats: Dict = card.get_card_info()
    name_of_enemy.append(stats["name"])

print("Turn execution:")
print(f"Strategy: {aggressiveStrategy.__class__.__name__}")

actions: Dict = aggressiveStrategy.execute_turn(
    list(enemy.values()),
    name_of_enemy,
)

print(f"Actions: {actions}\n")

print("Game Report:")

report: Dict = Engine.get_engine_status()
print(f"{report}\n")

print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
