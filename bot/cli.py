# bot/cli.py
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Binance Futures order bot")
    parser.add_argument("--symbol", required=True, help="Trading symbol, e.g. BTCUSDT")
    parser.add_argument("--side", required=True, type=str.upper, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, dest="type", type=str.upper, choices=["MARKET", "LIMIT"], help="Order type")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit order price")
    return parser.parse_args()
