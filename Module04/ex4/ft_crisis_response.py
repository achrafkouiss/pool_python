# ######################ex4##################
def recover_archive(file_name):
    print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
    with open(file_name, 'r') as file:
        r = file.read()
        print(f"SUCCESS: Archive recovered - ''{r}''")
        print("STATUS: Normal operations resumed\n")


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    try:
        recover_archive('lost_archive.txt')
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(e)

    try:
        recover_archive('classified_vault.txt')
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(type(e))

    try:
        recover_archive('standard_archive.txt')
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception as e:
        print(e)

    print("All crisis scenarios handled successfully. Archives secure.")


main()
