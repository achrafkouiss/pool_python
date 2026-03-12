from enum import Enum
from typing import List, Dict

from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


class Rarity(Enum):
    COMMON: str = "Common"
    UNCOMMON: str = "Uncomon"
    RARE: str = "Rare"
    ELITE: str = "Elite"
    LEGENDARY: str = "Lgendary"


print("\n=== DataDeck Tournament Platform ===\n")

print("Registering Tournament Cards...\n")

dragon_001: TournamentCard = TournamentCard(
    "dragon_001",
    5,
    "Elite",
    10,
    15,
)

wizard_001: TournamentCard = TournamentCard(
    "wizard_001",
    4,
    "Rare",
    9,
    7,
)

tournament: TournamentPlatform = TournamentPlatform()

print("Fire Dragon (ID: dragon_001):")
print(tournament.register_card(dragon_001))

print("\nIce Wizard (ID: wizard_001):")
print(tournament.register_card(wizard_001))

print("Creating tournament match...")

match: Dict = tournament.create_match(
    "dragon_001",
    "wizard_001",
)

print(f"Match result: {match}\n")

print("Tournament Leaderboard:")

leaderboard: List[Dict] = tournament.get_leaderboard()

for entry in leaderboard:
    print(
        f"{entry['rank']}. {entry['name']} - "
        f"Rating: {entry['rating']} ({entry['record']})"
    )

print("\nPlatform Report:")
print(f"{tournament.generate_tournament_report()}\n")

print("=== Tournament Platform Successfully Deployed! ===")
print("All abstract patterns working together harmoniously!")
