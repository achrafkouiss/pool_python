artifacts = [
    {"name": "Storm Crown", "power": 74, "type": "accessory"},
    {"name": "Wind Cloak", "power": 86, "type": "focus"},
    {"name": "Storm Crown", "power": 88, "type": "focus"},
    {"name": "Earth Shield", "power": 112, "type": "accessory"},
]

mages = [
    {"name": "Alex", "power": 98, "element": "fire"},
    {"name": "Morgan", "power": 77, "element": "wind"},
    {"name": "Rowan", "power": 80, "element": "wind"},
    {"name": "Alex", "power": 64, "element": "shadow"},
    {"name": "Casey", "power": 81, "element": "lightning"},
]

spells = ["darkness", "heal", "tsunami", "shield"]


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
        )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: "* " + x + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max_power": max(mages, key=lambda m: m["power"])["power"],
        "min_power": min(mages, key=lambda m: m["power"])["power"],
        "avg_power": round(
            sum(map(lambda m: m["power"], mages)) / len(mages), 2
            ),
    }


def main() -> None:
    artifacts_list = artifact_sorter(artifacts)

    print("\nTesting artifact sorter...\n")
    for index in range(len(artifacts_list) - 1):
        print(
            f"{artifacts_list[index]['name']} "
            f"({artifacts_list[index]['power']} power)"
            " comes before "
            f"{artifacts_list[index + 1]['name']}"
            f" ({artifacts_list[index + 1]['power']} power)"
        )

    print("\nTesting spell transformer...")
    print(*spell_transformer(spells))


if __name__ == "__main__":
    main()
