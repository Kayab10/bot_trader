# bot/validators.py
"""Validator helpers for trading bot inputs."""


def validate_symbol(symbol):
    """Validate and normalize a trading symbol.

    Args:
        symbol (str): Raw trading symbol input.

    Returns:
        str: Normalized symbol in uppercase.

    Raises:
        ValueError: If symbol is missing or contains invalid characters.
    """
    if not symbol or not symbol.strip():
        raise ValueError("Symbol must be provided")
    normalized_symbol = symbol.strip().upper()
    if not normalized_symbol.isalnum():
        raise ValueError("Symbol must contain only letters and numbers")
    return normalized_symbol


def validate_side(side):
    """Validate and normalize the order side."""
    normalized_side = side.strip().upper()
    if normalized_side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL")
    return normalized_side


def validate_order_type(order_type):
    """Validate and normalize the order type."""
    normalized_type = order_type.strip().upper()
    if normalized_type not in {"MARKET", "LIMIT"}:
        raise ValueError("Type must be MARKET or LIMIT")
    return normalized_type


def validate_quantity(quantity):
    """Validate that quantity is provided and positive."""
    if quantity is None:
        raise ValueError("Quantity must be provided")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    return quantity


def validate_price(price, order_type):
    """Validate price requirements based on order type."""
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        return price
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0")
    return price
