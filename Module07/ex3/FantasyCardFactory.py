from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory
import random

class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        creature_names = [
            "Fire Dragon",
            "Goblin Warrior",
            "Ice Wizard",
            "Lightning Elemental",
            "Stone Golem",
            "Shadow Assassin",
            "Healing Angel",
            "Forest Sprite"
            ]
        if isinstance(name_or_power, str):
            name = name_or_power
            cost = random.randint(1, 5)
        elif isinstance(name_or_power, int):
            name = random.choice(creature_names)
            cost = name_or_power
        stats = {
            "common": {
                "name": name, 
                "cost": cost,
                "rarity": "Common",
                "attack": random.randint(1, 3),
                "health": random.randint(1, 3)
                },
            "uncomon": {
                "name": name, 
                "cost": cost,
                "rarity": "Uncomon",
                "attack": random.randint(3, 5),
                "health": random.randint(3, 5)
                },
            "rare": {
                "name": name, 
                "cost": cost,
                "rarity": "Rare",
                "attack": random.randint(5, 8),
                "health": random.randint(5, 8)
                },
            "elite": {
                "name": name, 
                "cost": cost,
                "rarity": "ELITE",
                "attack": random.randint(8, 10),
                "health": random.randint(8, 10)
                },
            "lengendary": {
                "name": name, 
                "cost": cost,
                "rarity": "Lgendary",
                "attack": random.randint(10, 12),
                "health": random.randint(10, 12)
                }
        }
        random_key = random.choice(list(stats.keys()))
        random_rarity = stats[random_key] 
        return CreatureCard(**random_rarity)


    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        spells = {
            "Lightning Bolt": "damage",
            "Healing Potion": "heal",
            "Fireball": "damage",
            "Shield Spell": "buff",
            "Meteor": "damage",
            "Ice Shard": "damage",
            "Divine Light": "heal",
            "Magic Missile": "damage"
        }
        if isinstance(name_or_power, str):
            list_of_types = ["damage", "heal", "buff",]
            name = name_or_power
            effect_type = random.choice(list_of_types)
        elif isinstance(name_or_power, int):
            random_key = random.choice(list(spells.keys()))
            name = random_key
            effect_type = spells[name]
        stats = {
            "common": {
                "name": name,
                "cost": random.randint(1, 5),
                "rarity": "Common",
                "effect_type": effect_type,
                },
            "uncomon": {
                "name": name, 
                "cost": random.randint(1, 5),
                "rarity": "Uncomon",
                "effect_type": effect_type
                },
            "rare": {
                "name": name, 
                "cost": random.randint(1, 5),
                "rarity": "Rare",
                "effect_type": effect_type
                },
            "elite": {
                "name": name, 
                "cost": random.randint(1, 5),
                "rarity": "Elite",
                "effect_type": effect_type
                },
            "lengendary": {
                "name": name, 
                "cost": random.randint(1, 5),
                "rarity": "Lgendary",
                "effect_type": effect_type
                }
        }
        random_key = random.choice(list(stats.keys()))
        random_rarity = stats[random_key] 
        return SpellCard(**random_rarity)


    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        artifact_names = [
            "Mana Crystal",
            "Sword of Power",
            "Ring of Wisdom",
            "Shield of Defense",
            "Crown of Kings",
            "Boots of Speed",
            "Cloak of Shadows",
            "Staff of Elements"
            ]
        effect = [
            "Permanent: +1 mana per turn",
            "Permanent: +2 attack to equipped creature",
            "Permanent: Draw an extra card each turn",
            "Permanent: +3 health to all friendly creatures",
            "Permanent: +1 cost reduction to all cards",
            "Permanent: Cards cost 1 less mana",
            "Permanent: Creatures have stealth",
            "Permanent: +1 spell damage"
            ]
        if isinstance(name_or_power, str):
            name = name_or_power
            durability = random.randint(1, 10)
        elif isinstance(name_or_power, int):
            name = random.choice(artifact_names)
            durability = name_or_power
        effect_type = random.choice(effect)
        stats = {
            "common": {
                "name": name,
                "cost": random.randint(1, 5),
                "rarity": "Common",
                "durability": durability,
                "effect": effect_type
                },
            "uncomon": {
                "name": name, 
                "cost": random.randint(1, 5),
                "rarity": "Uncomon",
                "durability": durability,
                "effect": effect_type
                },
            "rare": {
                "name": name, 
                "cost": random.randint(1, 5),
                "rarity": "Rare",
                "durability": durability,
                "effect": effect_type
                },
            "elite": {
                "name": name, 
                "cost": random.randint(1, 5),
                "rarity": "Elite",
                "durability": durability,
                "effect": effect_type
                },
            "lengendary": {
                "name": name, 
                "cost": random.randint(1, 5),
                "rarity": "Lgendary",
                "durability": durability,
                "effect": effect_type
                }
        }
        random_key = random.choice(list(stats.keys()))
        random_rarity = stats[random_key] 
        return ArtifactCard(**random_rarity)

    def create_themed_deck(self, size: int) -> dict:
        methods_list = [
            self.create_creature,
            self.create_spell,
            self.create_artifact
            ]
        deck = {}
        for index in range(size):
            methode = random.choice(methods_list)
            card = methode(random.randint(1, 10)) 
            deck.update({index:card})
        return deck

    def get_supported_types(self) -> dict:
        support_card = {}
        methods_list = [
            self.create_spell,
            self.create_artifact
            ] 
        methode = random.choice(methods_list)
        card = methode(random.randint(1, 10)) 
        support_card.update({card.__class__.__name__:card})
        return support_card
