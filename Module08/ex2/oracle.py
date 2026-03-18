import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from the .env file into the process environment
load_dotenv()

# Required environment variables for the application to run
required_vars = {
    "MATRIX_MODE",
    "DATABASE_URL",
    "API_KEY",
    "LOG_LEVEL",
    "ZION_ENDPOINT"
}

# Determine which required variables are missing
# os.environ contains all environment variables currently loaded
missing_vars = required_vars - set(os.environ)

# If some variables are missing, report the error and stop execution
if missing_vars:
    print("ORACLE STATUS: Configuration error\n")
    print("Missing environment variables:")
    for var in missing_vars:
        print(f"- {var}")
    print("\nCheck your .env file or environment configuration.")
    exit(1)

print("ORACLE STATUS: Reading the Matrix...\n")

# Retrieve environment variable values
mode = os.getenv("MATRIX_MODE")
database = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")
log_level = os.getenv("LOG_LEVEL")
zion = os.getenv("ZION_ENDPOINT")

print("Configuration loaded:")
print(f"Mode: {mode}")

# Simple validation of the database connection string
print("Database:", end=" ")
if database.startswith("https://"):
    print("Connected to local instance")
else:
    print("Connection string looks invalid")

# Simulated list of valid API keys for authentication
data = ["bacd1234", "acdb1234", "abcd1234", "bcda1234"]

# Check if the provided API key matches a known key
print("API Access:", end=" ")
if api_key in data:
    print("Authenticated")
else:
    print("Unauthenticated")

# Display logging level configured for the application
print(f"Log Level: {log_level}")

# Check if the Zion network endpoint is defined
print("Zion Network:", end=" ")
if zion:
    print("Online\n")
else:
    print("Offline\n")

print("Environment security check:")

# # Verify that a .env configuration file exists in the current directory
env_path = find_dotenv()
if env_path and os.path.exists(env_path):
    print("[OK] .env file detected")
else:
    print("[WARNING] .env file missing")

# Verify that an API key was actually loaded
if api_key != "":
    print("[OK] API key loaded from environment")
else:
    print("[WARNING] API key not configured")

# Validate the environment mode
if mode in ["development", "production"]:
    print("[OK] Environment mode valid")
else:
    print("[WARNING] Unknown MATRIX_MODE value")

print("\nThe Oracle sees all configurations.")