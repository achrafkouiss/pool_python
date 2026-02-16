# ######################ex2##################
import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")


id = input("Input Stream active. Enter archivist ID: ")
report = input("Input Stream active. Enter status report: ")

sys.stdout.write("\n{[}STANDARD{]} Archive status from ")
sys.stdout.write(f"{id} : ")
sys.stdout.write(f"{report}\n")

sys.stderr.write("{[}ALERT{]} System diagnostic: ")
sys.stderr.write("Communication channels verified\n")
sys.stdout.write("{[}STANDARD{]} Data transmission complete\n")

print("\nThree-channel communication test successful.")
