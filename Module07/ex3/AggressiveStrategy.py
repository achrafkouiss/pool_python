from typing import List
from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played: List[str] = []
        damage_dealt: int = 0
        mana_used: int = 0
        mana: int = 10

        for card in hand:
            stats = card.get_card_info()

            if card.__class__.__name__ == "CreatureCard":
                damage_dealt += stats["attack"]
                cards_played.append(stats["name"])
                mana_used += stats["cost"]
                mana -= mana_used

            elif card.__class__.__name__ == "ArtifactCard":
                if "attack" in stats["effect"]:
                    cards_played.append(stats["name"])
                    damage_dealt += 1
                    mana_used += stats["cost"]
                    mana -= mana_used

            elif card.__class__.__name__ == "SpellCard":
                if stats["effect_type"] == "damage":
                    cards_played.append(stats["name"])
                    damage_dealt += stats["cost"]
                    mana_used += stats["cost"]
                    mana -= mana_used

            if mana <= 0:
                break

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": battlefield,
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return f"Factory: {self.__class__.__name__}"

    def prioritize_targets(self, available_targets: list) -> list:
        priority_targets: List = []

        if not available_targets:
            return []

        for target in available_targets:
            if target.__class__.__name__ == "CreatureCard":
                priority_targets.append(target)

        if not priority_targets:
            priority_targets = available_targets

        return priority_targets
