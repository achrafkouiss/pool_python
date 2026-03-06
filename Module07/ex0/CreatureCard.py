from .Card import Card

class CreatrueCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int):
        super().__init__(name, cost, rarity)
        ## the probleme here is that i could not raise (try/except is not autorized)
        # if attack < 0 or health < 0:
        #     raise ValueError("attack and health must be positive integers")
        self.attack = attack if attack > 0 else 0
        self.health = health if health > 0 else 0

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            return {
                "error": "game_state should contain mana as a key",
            }
        if self.is_playable(game_state["mana"]):
            return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": "Cannot summon Creature to battlefield because of"\
                  " insufficient mana",
        }
    
    def attack_target(self, target: Card) -> dict:
        target.health = max(0, target.health - self.attack)         
        return {
            "attacker": self.name,
            "target": target.name,
            "damage_dealt": self.attack,
            "combat_resolved": target.health <= 0
        }
