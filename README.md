# Bot Trader

A friendly command-line trading bot for Binance Futures testnet.

This project is designed to let you place simple market and limit futures orders from the terminal while keeping the request flow clean, validated, and logged.

## What it does

- Reads Binance API credentials from a `.env` file
- Supports `MARKET` and `LIMIT` futures orders
- Validates user inputs before sending requests
- Sends orders through Binance Futures testnet using the Binance Python client
- Logs request and response details to separate files for market and limit orders
- Displays a clear order summary or failure message in the terminal

## Why it exists

This bot is useful when you want a lightweight tool to test order placement without building a full trading system. It focuses on:

- simple CLI order entry
- input validation for safety
- logging for auditability
- a small, reusable client wrapper around Binance credentials

## Quick start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Create a `.env` file

In the project root, create a file named `.env` and add your Binance testnet values:

```env
API_KEY=your_api_key
API_SECRET=your_api_secret
BASE_URL=https://testnet.binancefuture.com
```

> `BASE_URL` is optional. If set, it overrides the default Binance testnet endpoints.

### 3. Place an order

#### Market order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

#### Limit order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 100000
```

## Command-line options

- `--symbol` : Trading pair symbol, e.g. `BTCUSDT`
- `--side` : `BUY` or `SELL`
- `--type` : `MARKET` or `LIMIT`
- `--quantity` : Order quantity (must be greater than 0)
- `--price` : Price for `LIMIT` orders

## How it works

### Entry point

- `main.py` is the application entry point.
- It parses CLI arguments, validates them, and routes the order to the correct handler.
- Errors are handled cleanly and printed as friendly failure messages.

### Core components

- `bot/cli.py` : Parses the command-line arguments using `argparse`.
- `bot/client.py` : Loads `.env` credentials and initializes the Binance Futures client.
- `bot/orders.py` : Contains helpers for placing market or limit orders.
- `bot/validators.py` : Ensures symbol, side, order type, quantity, and price are valid.
- `bot/logging_config.py` : Sets up logging and writes order activity to `logs/market_order.log` and `logs/limit_order.log`.

### Logging behavior

- All order requests and responses are written to files under the `logs/` folder.
- Market orders are logged to `logs/market_order.log`.
- Limit orders are logged to `logs/limit_order.log`.

## File structure

- `main.py` — app entry point
- `bot/cli.py` — CLI argument parser
- `bot/client.py` — Binance client wrapper
- `bot/orders.py` — order placement logic
- `bot/validators.py` — input validation
- `bot/logging_config.py` — logger setup
- `logs/` — generated logs for order activity

## Notes

- This tool is intended for Binance Futures testnet usage.
- Make sure your API keys are kept secure and not committed to source control.
- Use the `BASE_URL` value only when pointing to a testnet or custom endpoint.

## Troubleshooting

- If the bot reports `API_KEY and API_SECRET must be set in .env`, confirm the `.env` file exists in the project root.
- If you receive a Binance API error, verify your testnet keys and market symbol.
- If network errors occur, check your internet connection and Binance testnet availability.
