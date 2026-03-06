from ex0.Card import Card
from ex2 import Magical, Combatable

class EliteCard(Card, Magical, Combatable):
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        pass

    def channel_mana(self, amount: int) -> dict:
        pass

    def get_magic_stats(self) -> dict:
        pass

    def attack(self, target) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass

    def play(self, game_state: dict) -> dict:
        pass
