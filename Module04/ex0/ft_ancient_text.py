# ######################ex0##################
file = open('ancient_fragment.txt', 'r')

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

print(f"Accessing Storage Vault: {file.name}")
print("Connection established...\n")

print("RECOVERED DATA:")
print(file.read(), "\n")

print("Data recovery complete. Storage unit disconnected.")
file.close()
