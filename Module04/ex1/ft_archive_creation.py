# ######################ex1##################
print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

data = [
    "{[}ENTRY 001{]} New quantum algorithm discovered",
    "{[}ENTRY 002{]} Efficiency increased by 347%",
    "{[}ENTRY 003{]} Archived by Data Archivist trainee"
    ]

file = open("new_discovery.txt", 'w')

print(f"Initializing new storage unit: {file.name}")
print("Storage unit created successfully...\n")


print("Inscribing preservation data...")
for element in data:
    print(element)
    file.write(element + "\n")

print("\nData inscription complete. Storage unit sealed.")
print(f"Archive '{file.name}' ready for long-term preservation")
file.close()
