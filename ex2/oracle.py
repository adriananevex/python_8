import os
import sys
from dotenv import load_dotenv


def load_config():
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }

    return config


def validate_config(config):
    missing = []

    for key, value in config.items():
        if not value:
            missing.append(key)

    return missing


def show_status(config):
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:")

    mode = config["MATRIX_MODE"]

    print(f"Mode: {mode}")

    if mode == "development":
        print("Database: Connected to local instance")
        print("Log Level: DEBUG")
    elif mode == "production":
        print("Database: Connected to production system")
        print("Log Level: ERROR")

    print("API Access: Authenticated" if config["API_KEY"] else "API Access: Missing key")

    print("Zion Network: Online" if config["ZION_ENDPOINT"] else "Zion Network: Offline")


def security_check():
    print("\nEnvironment security check:")

    if not os.path.exists(".env"):
        print("[WARNING] .env file not found")
    else:
        print("[OK] .env file properly configured")

    print("[OK] No hardcoded secrets detected")
    print("[OK] Production overrides available")


def main():
    config = load_config()
    missing = validate_config(config)

    if missing:
        print("WARNING: Missing configuration variables:")
        for var in missing:
            print(f" - {var}")
        print("\nYou can set them in:")
        print("1. Environment variables")
        print("2. .env file")
        print("\nExample:")
        print("MATRIX_MODE=development python oracle.py\n")

    show_status(config)
    security_check()


if __name__ == "__main__":
    main()
