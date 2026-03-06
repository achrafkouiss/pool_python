from ex0.Card import Card

class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int, effect: str):
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            return {
                "error": "game_state should contain mana as a key",
            }
        if self.is_playable(game_state["mana"]):
            return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": "Insufficient mana",
        }

    def activate_ability(self) -> dict:
        return {"effect": self.effect}
