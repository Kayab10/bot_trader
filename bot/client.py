# bot/client.py
import os

from dotenv import load_dotenv
from binance.client import Client


class BinanceClient:
    def __init__(self, api_key=None, api_secret=None, base_url=None):
        load_dotenv()
        self.api_key = api_key or os.getenv("API_KEY")
        self.api_secret = api_secret or os.getenv("API_SECRET")
        self.base_url = base_url or os.getenv("BASE_URL")

        if not self.api_key or not self.api_secret:
            raise ValueError("API_KEY and API_SECRET must be set in .env")

        self.client = Client(self.api_key, self.api_secret, testnet=True)
        if self.base_url:
            self.client.API_URL = self.base_url
            self.client.FUTURES_URL = self.base_url

    def create_market_order(self, symbol, side, quantity):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

    def create_limit_order(self, symbol, side, quantity, price):
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )
