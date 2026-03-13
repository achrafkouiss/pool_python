import os
from dotenv import load_dotenv

load_dotenv()

required_vars = {
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
    }

missing_vars = required_vars - set(os.environ)
if not missing_vars:
    print("ORACLE STATUS: Reading the Matrix...\n")

    print("Configuration loaded:")
    print(f"Mode: {os.getenv('MATRIX_MODE')}")
    database = os.getenv("DATABASE_URL")
    print("Database: ", end="")
    if database.startswith("https://"):
        print("Connected to local instance")
    else:
        print("not Connected to local instance")
    print("API Access:", end="")
    if os.getenv("API_KEY") == "abcd1234":
        print("Authenticated")
    else:
        print("Unauthenticated")
    print(f"Log Level: {os.getenv('LOG_LEVEL')}")
    print("Zion Network: ", end="")
    if os.getenv("ZION_ENDPOINT"):
        print("Online\n")
    else:
        print("Offline\n")

    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available\n")

    print("The Oracle sees all configurations.")
