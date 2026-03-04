# from .spellbook import record_spell

def validate_ingredients(ingredients: str) -> str:
    ingredients_list = ingredients.split(" ")
    for element in ingredients_list:
        if element not in ["fire", "water", "earth", "air"]:
            return f"{ingredients} - INVALID"
    return f"{ingredients} - VALID"
