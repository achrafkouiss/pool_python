from ex0.Card import Card
from ex2 import Magical, Combatable

class EliteCard(Card, Combatable, Magical,):
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass

    def attack(self, target: Card) -> dict:
        return {
            "attacker": self.name,
            "target": target.name,
            "damage": self.cost,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        alive = max(0, self.cost - incoming_damage)         
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.cost - incoming_damage,
            "still_alive": alive >= 0
        }

    def get_combat_stats(self) -> dict:
        pass

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            return {
                "error": "game_state should contain mana as a key",
            }
        if self.is_playable(game_state["mana"]):
            return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "EliteCard is played",
        }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": "Cannot play EliteCard insufficient mana"
        }
    
