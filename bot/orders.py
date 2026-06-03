# bot/orders.py
"""Order placement utilities for the trading bot."""

def place_market_order(client, symbol, side, quantity):
    """Submit a market order using the provided Binance client.

    Args:
        client (BinanceClient): Binance client instance.
        symbol (str): Trading symbol, e.g. BTCUSDT.
        side (str): Order side, BUY or SELL.
        quantity (float): Quantity to trade.

    Returns:
        dict: Binance order response.
    """
    return client.create_market_order(symbol=symbol, side=side, quantity=quantity)


def place_limit_order(client, symbol, side, quantity, price):
    """Submit a limit order using the provided Binance client.

    Args:
        client (BinanceClient): Binance client instance.
        symbol (str): Trading symbol, e.g. BTCUSDT.
        side (str): Order side, BUY or SELL.
        quantity (float): Quantity to trade.
        price (float): Limit order price.

    Returns:
        dict: Binance order response.
    """
    return client.create_limit_order(symbol=symbol, side=side, quantity=quantity, price=price)
