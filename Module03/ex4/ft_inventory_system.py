data_dictionary = {
    "players": {
        "alice": {
            "items": {
                "pixel_sword": 1,
                "code_bow": 1,
                "health_byte": 2,
                "quantum_ring": 3,
            },
            "total_value": 1900,
            "item_count": 7,
        },
        "bob": {
            "items": {"code_bow": 3, "pixel_sword": 2},
            "total_value": 900,
            "item_count": 5,
        },
        "charlie": {
            "items": {"pixel_sword": 1, "code_bow": 1},
            "total_value": 350,
            "item_count": 2,
        },
        "diana": {
            "items": {
                "code_bow": 3,
                "pixel_sword": 3,
                "health_byte": 3,
                "data_crystal": 3,
            },
            "total_value": 4125,
            "item_count": 12,
        },
    },
    "catalog": {
        "pixel_sword": {
            "type": "weapon",
            "value": 150,
            "rarity": "common"
            },
        "quantum_ring": {
            "type": "accessory",
            "value": 500,
            "rarity": "rare"
            },
        "health_byte": {
            "type": "consumable",
            "value": 25,
            "rarity": "common"
            },
        "data_crystal": {
            "type": "material",
            "value": 1000,
            "rarity": "legendary"
            },
        "code_bow": {
            "type": "weapon",
            "value": 200,
            "rarity": "rare"
            },
    }
}


player = data_dictionary["players"]


def player_exist(name):
    if player.get(name):
        return True
    else:
        return False


def inventory(name):
    dict = {}
    if player_exist(name):
        for key, qty in player[name]["items"].items():
            ty = data_dictionary["catalog"][key]["type"]
            rarity = data_dictionary["catalog"][key]["rarity"]
            value = data_dictionary["catalog"][key]["value"]
            total = qty * value
            print(
                f"{key} ({ty}, {rarity}):  {qty}x @ {value}"
                + f" gold each = {total} gold"
            )
            if ty in dict:
                type_qty = dict[ty] + qty
            else:
                type_qty = qty
            dict.update({ty: type_qty})
        total_value = player[name]["total_value"]
        item_count = player[name]["item_count"]
        print(f"\nInventory value:  {total_value} gold")
        print(f"Item count:  {item_count} items")
        print("Categories:  ", end="")
    for type, quantity in dict.items():
        print(f"{type}({quantity}) ", end="")
    print("\n")


def Transaction(player1, player2, items: dict):
    dictionary = {}
    if player_exist(player1) and player_exist(player2):
        for item, qty in items.items():
            if item in player[player1]["items"]:
                if qty <= player[player1]["items"][item]:
                    dictionary.update({item: qty})
    if len(dictionary) == len(items):
        for type, quantity in dictionary.items():
            if quantity <= player[player1]["items"][type]:
                if type in player[player2]["items"]:
                    player2_qty = player[player2]["items"][type] + quantity
                else:
                    player2_qty = quantity
                player1_qty = player[player1]["items"][type] - quantity
                player[player1]["items"].update({type: player1_qty})
                player[player2]["items"].update({type: player2_qty})
        print("Transaction successful!\n")
    else:
        print("probleme with the Transaction\n")


def display_inventory(item):
    for name, items in player.items():
        if item in items["items"]:
            print(f"{name} {item}:  {items['items'].get(item)}")


def stats():
    valuable_playe = {}
    valuable_item = {}
    for name, items in player.items():
        valuable_playe.update({name: items["total_value"]})
        valuable_item.update({name: len(items["items"])})
    if len(valuable_playe) > 0:
        for elem in valuable_playe.values():
            max_value = elem
        for total_value in valuable_playe.values():
            if max_value < total_value:
                max_value = total_value
        for na, va in valuable_playe.items():
            if va == max_value:
                player_name = na
        print(f"Most valuable player:  {player_name} ({max_value} gold)")
    if len(valuable_item) > 0:
        for elem in valuable_item.values():
            item_count = elem
        for total_count in valuable_item.values():
            if item_count < total_count:
                item_count = total_count
        for na, va in valuable_item.items():
            if va == item_count:
                name_player = na
        print(f"Most items:  {name_player} ({item_count} items)")
    list = []
    for x, y in data_dictionary["catalog"].items():
        if y["rarity"] == "rare":
            list += [x]
    print("Rarest items:  ", end="")
    if len(list):
        for elem in list:
            if elem != list[-1]:
                print(f"{elem}, ", end="")
            else:
                print(f"{elem}")
    else:
        print("none")


def main():
    print("=== Player Inventory System ===\n")

    print("=== Alice's Inventory ===\n")
    inventory("alice")

    print("=== Transaction:  Alice gives Bob 2 potions ===")
    Transaction("alice", "charlie", {"health_byte": 2})
    print("=== Updated Inventories ===")
    display_inventory("health_byte")

    print("\n=== Inventory Analytics ===")
    stats()


main()
