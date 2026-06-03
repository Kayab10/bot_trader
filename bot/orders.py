# bot/orders.py

def place_market_order(client, symbol, side, quantity):
    return client.create_market_order(symbol=symbol, side=side, quantity=quantity)


def place_limit_order(client, symbol, side, quantity, price):
    return client.create_limit_order(symbol=symbol, side=side, quantity=quantity, price=price)
