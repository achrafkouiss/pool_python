data_dictionary = {
   "alice": [
      "first_kill",
      "level_10",
      "treasure_hunter",
      "first_kill",
      "speed_demon"
   ],
   "bob": [
      "first_kill",
      "level_10",
      "boss_slayer",
      "collector",
      "first_kill",
      "collector"
   ],
   "charlie": [
      "level_10",
      "treasure_hunter",
      "boss_slayer",
      "speed_demon",
      "perfectionist"
   ]
}

alice = set(data_dictionary["alice"])
bob = set(data_dictionary["bob"])
charlie = set(data_dictionary["charlie"])
print("=== Achievement Tracker System ===\n")
print(f"Player alice achievements: {alice}")
print(f"Player bob achievements: {bob}")
print(f"Player charlie achievements: {charlie}")

unique_ach = alice.union(bob, charlie)
print("\n=== Achievement Analytics ===")
print(f"All unique achievements: {unique_ach}")
print(f"Total unique achievements: {len(unique_ach)}\n")

common = alice.intersection(bob, charlie)
alice_diff = alice.difference(bob, charlie)
bob_diff = bob.difference(alice, charlie)
charlie_diff = charlie.difference(bob, alice)
unique = alice_diff.union(bob_diff, charlie_diff)
print(f"Common to all players: {common}")
print(f"Rare achievements (1 player): {unique}\n")

alice_bob_common = alice.intersection(bob)
alice_unique = alice.difference(bob)
bob_unique = bob.difference(alice)
print(f"Alice vs Bob common: {alice_bob_common}")
print(f"Alice unique: {alice_unique}")
print(f"Bob unique: {bob_unique}")
