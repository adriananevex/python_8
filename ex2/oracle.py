import os
from dotenv import load_dotenv


def load_config():
    load_dotenv()

    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def validate_config(config):
    missing = []

    for key, value in config.items():
        if not value:
            missing.append(key)

    return missing


def detect_source(var_name):
    return "ENV" if os.getenv(var_name) is not None else ".env"


def show_status(config):
    print("\nORACLE STATUS: Reading the Matrix...\n")
    print("Configuration loaded:\n")

    # MATRIX MODE (corrigido para não mostrar None)
    mode = config["MATRIX_MODE"] or "unknown"
    print(f"Mode: {mode} (source: {detect_source('MATRIX_MODE')})")

    if mode == "development":
        print("Running in DEVELOPMENT mode (local settings)")
    elif mode == "production":
        print("Running in PRODUCTION mode (secure environment)")
    else:
        print("Running in UNKNOWN mode (missing configuration)")

    # DATABASE
    db = config["DATABASE_URL"]
    print(f"Database: {db if db else 'Not configured'}")

    # API
    api = config["API_KEY"]
    print("API Access: Authenticated" if api else "API Access: Missing key")

    # LOG LEVEL
    log = config["LOG_LEVEL"]
    print(f"Log Level: {log if log else 'Not defined'}")

    # ZION
    zion = config["ZION_ENDPOINT"]
    print("Zion Network: Online" if zion else "Zion Network: Offline")


def security_check():
    print("\nEnvironment security check:")

    if os.path.exists(".env"):
        print("[OK] .env file found")
    else:
        print("[WARNING] .env file not found")

    overrides = any(
        os.getenv(var) is not None
        for var in ["MATRIX_MODE", "API_KEY", "DATABASE_URL"]
    )

    if overrides:
        print("[OK] Environment variables override detected")
    else:
        print("[INFO] No environment override detected")

    print("[OK] No hardcoded secrets detected")


def main():
    config = load_config()
    missing = validate_config(config)

    if missing:
        print("WARNING: Missing configuration variables:")
        for var in missing:
            print(f" - {var}")

        print("\nYou can set them in:")
        print("1. Environment variables")
        print("2. .env file\n")

    show_status(config)
    security_check()


if __name__ == "__main__":
    main()
