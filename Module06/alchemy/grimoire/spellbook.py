def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validation = validate_ingredients(ingredients)
    validation_list = validation.split()
    if validation_list[-1] != "VALID":
        return f"Spell rejected: {spell_name} ({validation})"
    return f"Spell recorded: {spell_name} ({validation})"
