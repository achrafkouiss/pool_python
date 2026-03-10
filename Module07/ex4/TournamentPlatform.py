from .TournamentCard import TournamentCard

class TournamentPlatform:
    def __init__(self):
        self.tournament_cards: list = []
        self.total_cards = 0
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        info = card.get_rank_info()
        string = ""
        for key, value in info.items():
            string += f"- {key}: {value}\n"
        self.tournament_cards.append(card)
        self.total_cards += 1
        return string
        

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        for card in self.tournament_cards:
            if card.name == card1_id:
                fist_card = card
            elif card.name == card2_id:
                second_card = card
        fist_card.play({"mana": 10})
        second_card.play({"mana": 10})
        index = 2
        while True:
            if index % 2:
                stat = fist_card.attack(second_card)
            else:
                stat = second_card.attack(fist_card)
            if not stat["alive"]:
                break
        if fist_card.name == stat["attacker"]:
            winner_rating = fist_card.calculate_rating()
            loser_rating = second_card.calculate_rating()
        elif second_card.name == stat["attacker"]:
            winner_rating = second_card.calculate_rating()
            loser_rating = fist_card.calculate_rating()
        self.matches_played += 1
        return {
            'winner': stat["attacker"],
            'loser': stat["defender"],
            'winner_rating': winner_rating,
            'loser_rating': loser_rating
            }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(
            self.tournament_cards,
            key=lambda card: card.calculate_rating(),
            reverse=True
        )

        leaderboard: list = []
        rank = 1

        for card in sorted_cards:
            stats = card.get_tournament_stats()
            leaderboard.append({
                "rank": rank,
                "name": stats["name"],
                "rating": stats["Rating"],
                "record": f"{stats['wins']}-{stats['loses']}"
            })
            rank += 1

        return leaderboard
            

    def generate_tournament_report(self) -> dict:
        total_rating: int = 0
        for card in self.tournament_cards:
            total_rating += card.calculate_rating()
        avg_rating = total_rating // self.total_cards
        return {
            'total_cards': self.total_cards,
            'matches_played': self.matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active'
            }