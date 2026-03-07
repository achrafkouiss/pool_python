from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
import random


class EliteCard(Card, Combatable, Magical):
    def __init__(
                    self, name: str,
                    cost: int,
                    rarity: str,
                    damage: int,
                    combat_type: str
                ) -> None:
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.combat_type = combat_type
        self.mana = 8

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


    def attack(self, target: str) -> dict:
        return {
                    "attacker": self.name,
                    "target": target,
                    "damage": self.damage,
                    "combat_type": self.combat_type,
               }

    def defend(self, incoming_damage: int) -> dict:
        blocked = random.randint(1, 10)
        alive = self.damage - incoming_damage + blocked
        return {
                    "defender": self.name,
                    "damage_taken": incoming_damage,
                    "damage_blocked": blocked,
                    "still_alive": alive > 0
               }

    def get_combat_stats(self) -> dict:
        return {
                    "dammage": self.damage,
                    "combat_type": self.combat_type,
                    "fight": True
               }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = 4
        self.mana -= mana_used
        return {
                    "caster": self.name,
                    "spell": spell_name,
                    "targets": targets,
                    "mana_used": mana_used,
               }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {"channeled": amount, "total_mana": self.mana}

    def get_magic_stats(self) -> dict:
        return {
                    "avalible_mana": self.mana,
                    "magic_potential": self.mana >= 5
               }
