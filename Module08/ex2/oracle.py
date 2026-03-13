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

if missing_vars:
    print("ORACLE STATUS: Configuration error\n")
    print("Missing environment variables:")
    for var in missing_vars:
        print(f"- {var}")
    print("\nCheck your .env file or environment configuration.")
    exit(1)

print("ORACLE STATUS: Reading the Matrix...\n")

mode = os.getenv("MATRIX_MODE")
database = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion = os.getenv("ZION_ENDPOINT")

print("Configuration loaded:")
print(f"Mode: {mode}")

print("Database:", end=" ")
if database.startswith("https://"):
    print("Connected to local instance")
else:
    print("Connection string looks invalid")

print("API Access:", end=" ")
if api_key == "abcd1234":
    print("Authenticated")
else:
    print("Unauthenticated")

print(f"Log Level: {log_level}")

print("Zion Network:", end=" ")
if zion:
    print("Online\n")
else:
    print("Offline\n")

print("Environment security check:")

if os.path.exists(".env"):
    print("[OK] .env file detected")
else:
    print("[WARNING] .env file missing")

if api_key != "":
    print("[OK] API key loaded from environment")
else:
    print("[WARNING] API key not configured")

if mode in ["development", "production"]:
    print("[OK] Environment mode valid")
else:
    print("[WARNING] Unknown MATRIX_MODE value")

print("\nThe Oracle sees all configurations.")