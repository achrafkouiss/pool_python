from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Dict, Optional, List, Any


class GameEngine:
    def __init__(self) -> None:
        self.deck: Dict = {}
        self.strategy_names: Optional[str]
        self.turns_simulated: int = 0
        self.card_created: int = 0
        self.damage: int = 0

    def configure_engine(
            self,
            factory: CardFactory,
            strategy: GameStrategy
            ) -> None:
        print(f"Factory: {factory.__class__.__name__}")
        print(f"Strategy: {strategy.__class__.__name__}")
        types: Dict[str, str] = {}
        creature: List[str] = []
        spell: List[str] = []
        artifact: List[str] = []
        self.deck = factory.create_themed_deck(5)
        self.card_created += len(self.deck)
        for card in self.deck.values():
            stats: Dict[str, Any] = card.get_card_info()
            if card.__class__.__name__ == "CreatureCard":
                creature.append(stats["name"])
            elif card.__class__.__name__ == "ArtifactCard":
                artifact.append(stats["name"])
            elif card.__class__.__name__ == "SpellCard":
                spell.append(stats["name"])
        types = {
            "creatures": creature if creature else "None",
            "spells": spell if spell else "None",
            "artifacts": artifact if artifact else "None",
        }
        self.strategy_names = strategy.__class__.__name__
        print(f"Available types:  {types}")

    def simulate_turn(self) -> dict:
        hand: Dict[str, int] = {}
        for card in self.deck.values():
            stats: Dict[str, Any] = card.get_card_info()
            hand.update({stats["name"]: stats["cost"]})
            if card.__class__.__name__ == "CreatureCard":
                self.damage += stats["attack"]
            elif card.__class__.__name__ == "ArtifactCard":
                self.damage += 1
            elif card.__class__.__name__ == "SpellCard":
                self.damage += 1
        self.turns_simulated += 1
        return hand

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": self.strategy_names,
            "total_damage": self.damage,
            "card_created": self.card_created,
        }
