# bot/validators.py

def validate_symbol(symbol):
    if not symbol or not symbol.strip():
        raise ValueError("Symbol must be provided")
    normalized_symbol = symbol.strip().upper()
    if not normalized_symbol.isalnum():
        raise ValueError("Symbol must contain only letters and numbers")
    return normalized_symbol


def validate_side(side):
    normalized_side = side.strip().upper()
    if normalized_side not in {"BUY", "SELL"}:
        raise ValueError("Side must be BUY or SELL")
    return normalized_side


def validate_order_type(order_type):
    normalized_type = order_type.strip().upper()
    if normalized_type not in {"MARKET", "LIMIT"}:
        raise ValueError("Type must be MARKET or LIMIT")
    return normalized_type


def validate_quantity(quantity):
    if quantity is None:
        raise ValueError("Quantity must be provided")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")
    return quantity


def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        return price
    if price is not None and price <= 0:
        raise ValueError("Price must be greater than 0")
    return price
