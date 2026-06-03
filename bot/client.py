# bot/client.py
import os

from dotenv import load_dotenv
from binance.client import Client


class BinanceClient:
    """Wrapper for Binance client interactions.

    This class loads API credentials from environment variables or accepts them
    directly and exposes methods to place market and limit futures orders.
    """

    def __init__(self, api_key=None, api_secret=None, base_url=None):
        """Initialize the Binance client with credentials and optional base URL.

        Args:
            api_key (str | None): Binance API key.
            api_secret (str | None): Binance API secret.
            base_url (str | None): Optional custom Binance API base URL.

        Raises:
            ValueError: If API_KEY or API_SECRET are missing.
        """
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
        """Create a futures market order on Binance.

        Args:
            symbol (str): Trading symbol, e.g. BTCUSDT.
            side (str): Order side, either BUY or SELL.
            quantity (float): Quantity to trade.

        Returns:
            dict: Binance order response.
        """
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity,
        )

    def create_limit_order(self, symbol, side, quantity, price):
        """Create a futures limit order on Binance.

        Args:
            symbol (str): Trading symbol, e.g. BTCUSDT.
            side (str): Order side, either BUY or SELL.
            quantity (float): Quantity to trade.
            price (float): Limit order price.

        Returns:
            dict: Binance order response.
        """
        return self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC",
        )
