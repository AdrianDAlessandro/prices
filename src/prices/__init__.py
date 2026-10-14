"""Daily stock prices from Yahoo Finance."""

from prices.load import TICKERS, load_prices

__all__ = ["TICKERS", "load_prices"]
