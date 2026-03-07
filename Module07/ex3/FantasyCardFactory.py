from ex0.Card import Card
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory

class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if  isinstance(name_or_power, str):
            # return Card(name_or_power, )
            pass

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

    def create_themed_deck(self, size: int) -> dict:
        pass

    def get_supported_types(self) -> dict:
        pass 
