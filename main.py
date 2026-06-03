# main.py
import requests

from binance.exceptions import BinanceAPIException
from bot.cli import parse_args
from bot.client import BinanceClient
from bot.logging_config import setup_logger
from bot.orders import place_limit_order, place_market_order
from bot.validators import (
    validate_order_type,
    validate_price,
    validate_quantity,
    validate_side,
    validate_symbol,
)


def format_success(symbol, side, order_type, quantity, response):
    output = [
        "=" * 20,
        "",
        "ORDER SUMMARY",
        "",
        f"Symbol: {symbol}",
        f"Side: {side}",
        f"Type: {order_type}",
        f"Quantity: {quantity}",
        "",
        f"Order ID: {response.get('orderId', 'N/A')}",
        f"Status: {response.get('status', 'N/A')}",
        f"Executed Qty: {response.get('executedQty', 'N/A')}",
        f"Average Price: {response.get('avgPrice', 'N/A')}",
        "",
        "SUCCESS",
        "",
        "=" * 20,
    ]
    print("\n".join(output))


def format_failure(reason):
    output = [
        "ORDER FAILED",
        "",
        "Reason:",
        reason,
    ]
    print("\n".join(output))


def main():
    logger = setup_logger()

    try:
        args = parse_args()
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        client = BinanceClient()

        logger.info(
            "ORDER REQUEST\nSymbol: %s\nSide: %s\nType: %s\nQuantity: %s\nPrice: %s",
            symbol,
            side,
            order_type,
            quantity,
            price if price is not None else "N/A",
        )

        if order_type == "MARKET":
            response = place_market_order(client, symbol, side, quantity)
        else:
            response = place_limit_order(client, symbol, side, quantity, price)

        logger.info("ORDER RESPONSE\n%s", response)
        format_success(symbol, side, order_type, quantity, response)
    except ValueError as exc:
        logger.error("VALIDATION ERROR\n%s", str(exc))
        format_failure(str(exc))
    except BinanceAPIException as exc:
        logger.error("BINANCE API ERROR\n%s", str(exc))
        format_failure(str(exc))
    except requests.exceptions.RequestException as exc:
        logger.error("NETWORK ERROR\n%s", str(exc))
        format_failure(str(exc))
    except Exception as exc:
        logger.error("UNEXPECTED ERROR\n%s", str(exc))
        format_failure("Unexpected error occurred")


if __name__ == "__main__":
    main()
