from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name, cost, rarity, damage, health):
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.health = health
        self.wins = 0
        self.loss = 0
        self.rate = self.calculate_rating()

    def play(self, game_state: dict) -> dict:
        if "mana" not in game_state:
            return {
                "error": "game_state should contain mana as a key",
            }
        if self.is_playable(game_state["mana"]):
            return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Card is  summoned to battlefield",
        }
        return {
            "card_played": self.name,
            "mana_used": 0,
            "effect": "Cannot summon cad to battlefield because of"\
                  " insufficient mana",
        }

    def attack(self, target) -> dict:
        card_stats = self.get_card_info()
        target_stats = target.get_card_info()
        combat: dict = {}
        if card_stats["damage"] >= target_stats["damage"]:
            combat = target.defend(card_stats["damage"])
            combat.update(
                {
                    "attacker": card_stats["name"],
                    "defender": target_stats["name"],
                    "damage": card_stats["damage"]
                    }
            )
        else:
            combat = self.defend(target_stats["damage"])
            combat.update(
                {
                    "attacker": target_stats["name"],
                    "defender": card_stats["name"],
                    "damage": target_stats["damage"]
                    }
            )
        if not combat["alive"]:
            if combat["attacker"] in card_stats:
                self.update_wins(1)
            elif combat["attacker"] in target_stats.values():
                target.update_wins(1)
        return combat

    def defend(self, incoming_damage: int) -> dict:
        self.health -= incoming_damage
        if self.health < 0:
            self.update_losses(1)
            return {
                "alive": False
            }
        return {
            "alive": True,
        }

    def calculate_rating(self) -> int:
        starting_scores: dict = {
            "Common": 1050,
            "Uncomon": 1100,
            "Rare": 1150,
            "Elite": 1200,
            "Lgendary": 2000
        }
        loses = 16 * self.loss
        wins = 16 * self.wins
        self.rate  = starting_scores[self.rarity] + wins - loses
        return self.rate

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "Rating": self.calculate_rating(),
            "wins": self.wins,
            "loses": self.loss,
        }

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.loss += losses

    def get_rank_info(self) -> dict:
        return {
            "Interfaces": [base.__name__ for base in self.__class__.__bases__],
            "Rating": self.calculate_rating(),
            "Record": f"{self.wins}-{self.loss}"
        }

    def get_combat_stats(self) -> dict:
        return {
            "name": self.name,
            "attack": self.damage,
            "health": self.health,
        }
