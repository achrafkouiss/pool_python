from .TournamentCard import TournamentCard
import random
from typing import List, Dict


class TournamentPlatform:
    def __init__(self):
        self.tournament_cards: List[TournamentCard] = []
        self.total_cards: int = 0
        self.matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        info: Dict = card.get_rank_info()
        string: str = ""
        for key, value in info.items():
            string += f"- {key}: {value}\n"
        self.tournament_cards.append(card)
        self.total_cards += 1
        return string

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        first_card: TournamentCard | None = None
        second_card: TournamentCard | None = None
        for card in self.tournament_cards:
            if card.name == card1_id:
                first_card = card
            elif card.name == card2_id:
                second_card = card
        if first_card is None or second_card is None:
            return {"error": "One or both cards not found in tournament."}
        first_card.play({"mana": 10})
        second_card.play({"mana": 10})
        attacker, defender = (
            (first_card, second_card)
            if random.choice([True, False])
            else (second_card, first_card)
        )
        while True:
            combat_result: Dict = attacker.attack(defender)
            if not combat_result["alive"]:
                break
            attacker, defender = defender, attacker
        if attacker.name == combat_result["attacker"]:
            winner_rating: int = attacker.calculate_rating()
            loser_rating: int = defender.calculate_rating()
        else:
            winner_rating = defender.calculate_rating()
            loser_rating = attacker.calculate_rating()
        self.matches_played += 1
        return {
            "winner": combat_result["attacker"],
            "loser": combat_result["defender"],
            "winner_rating": winner_rating,
            "loser_rating": loser_rating,
        }

    def get_leaderboard(self) -> list:
        sorted_cards = self.tournament_cards[:]

        n: int = len(sorted_cards)
        i: int = 0
        tmp: int = 0

        while i < n:
            j: int = i + 1
            while j < n:
                if (
                    sorted_cards[j].calculate_rating()
                    > sorted_cards[i].calculate_rating()
                ):
                    tmp = sorted_cards[i]
                    sorted_cards[i] = sorted_cards[j]
                    sorted_cards[j] = tmp
                j += 1
            i += 1

        leaderboard: list = []
        rank: int = 1

        for card in sorted_cards:
            stats = card.get_tournament_stats()
            leaderboard.append(
                {
                    "rank": rank,
                    "name": stats["name"],
                    "rating": stats["Rating"],
                    "record": f"{stats['wins']}-{stats['loses']}",
                }
            )
            rank += 1

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_rating: int = 0
        for card in self.tournament_cards:
            total_rating += card.calculate_rating()
        avg_rating: int = total_rating // self.total_cards
        return {
            "total_cards": self.total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
