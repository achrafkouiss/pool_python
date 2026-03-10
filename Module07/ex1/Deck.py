from ex0.Card import Card
import random
from typing import Dict, List


class Deck:
    def __init__(self):
        self.list_of_cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.list_of_cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.list_of_cards:
            if card.name == card_name:
                self.list_of_cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.list_of_cards)

    def draw_card(self) -> Card:
        card_drawed: Card = random.choice(self.list_of_cards)
        self.list_of_cards.remove(card_drawed)
        return card_drawed

    def get_deck_stats(self) -> dict:
        stats: Dict[str, float | int] = {
            "total_cards": len(self.list_of_cards),
            "creatures": 0,
            "spells": 0,
            "artifacts": 0,
            "avg_cost": 0,
        }
        totol_cost: int = 0
        for card in self.list_of_cards:
            if type(card).__name__ == "CreatureCard":
                stats["creatures"] += 1
            elif type(card).__name__ == "SpellCard":
                stats["spells"] += 1
            elif type(card).__name__ == "ArtifactCard":
                stats["artifacts"] += 1
            totol_cost += card.cost
        if stats["total_cards"]:
            stats["avg_cost"] = round(totol_cost / stats["total_cards"], 1)
        return stats
