import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")
BASE_URL = os.getenv("BASE_URL", "https://testnet.binancefuture.com")


def validate_config():
    if not API_KEY:
        raise ValueError("BINANCE_API_KEY is missing in .env file")

    if not API_SECRET:
        raise ValueError("BINANCE_API_SECRET is missing in .env file")

    if not BASE_URL:
        raise ValueError("BASE_URL is missing in .env file")