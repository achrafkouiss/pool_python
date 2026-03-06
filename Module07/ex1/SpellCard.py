from ex0.Card import Card

class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            return {
                "error": "game_state should contain mana as a key",
            }
        if self.effect_type == "damage":
            effect =  f"Deal {self.cost} damage to target"
        elif self.effect_type == "heal":
            effect =  f"heal {self.cost} health point to target"
        elif self.effect_type == "buff":
            effect =  f"buf {self.cost} to target"
        else:
            return {}
        if self.is_playable(game_state["mana"]):
            return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect
        }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": "Insufficient mana",
        }

    def resolve_effect(self, targets: list) -> dict:
        unaffected_targets: list = []
        count_unaffected_targets = 0
        for target in targets:
            stat = target.get_card_info()
            if not stat.get("health"):
                count_unaffected_targets += 1
                unaffected_targets.append(stat["name"])
        return {
            "unaffected_targets": unaffected_targets,
        }

            