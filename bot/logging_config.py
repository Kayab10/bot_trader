# bot/logging_config.py
import logging
from pathlib import Path


class OrderTypeFilter(logging.Filter):
    """Filter log records by the order type contained in the message."""

    def __init__(self, order_type):
        super().__init__()
        self.order_type = order_type

    def filter(self, record):
        """Return True when the record message matches the configured order type."""
        return self.order_type in record.getMessage()


def setup_logger():
    """Configure and return a logger for trading bot order events.

    The logger writes market and limit orders into separate files under `logs/`.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("trading_bot")
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)
    logs_dir = Path(__file__).resolve().parent.parent / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter("%(asctime)s\n%(message)s\n")

    market_handler = logging.FileHandler(logs_dir / "market_order.log", encoding="utf-8")
    market_handler.setFormatter(formatter)
    market_handler.addFilter(OrderTypeFilter("MARKET"))

    limit_handler = logging.FileHandler(logs_dir / "limit_order.log", encoding="utf-8")
    limit_handler.setFormatter(formatter)
    limit_handler.addFilter(OrderTypeFilter("LIMIT"))

    logger.addHandler(market_handler)
    logger.addHandler(limit_handler)

    return logger
