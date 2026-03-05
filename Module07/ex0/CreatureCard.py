from .Card import Card

class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        if attack < 0 or health < 0:
            raise ValueError("attack and health must be positive integers")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            raise ValueError("game_state shouls containe mana as a key")
        if not self.is_playable(game_state["mana"]):
            raise ValueError()
        card_info = self.get_card_info()
        return {
            "card_played": card_info["name"],
            "mana_used": card_info["cost"],
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target) -> dict:
        pass
