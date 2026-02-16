# ##################ex03#################
print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

print("Initiating secure vault access...")

with open('classified_data.txt', 'r+') as classified_data, \
     open('security_protocols.txt', 'r') as security_protocols:
    print("Vault connection established with failsafe protocols\n")

    print("SECURE EXTRACTION:")
    print(classified_data.read(), "\n")

    print("SECURE PRESERVATION:")
    last_line = security_protocols.read()
    classified_data.write(last_line)
    print(last_line)
    print("Vault automatically sealed upon completion\n")

print("All vault operations completed with maximum security.")
