"""Load daily prices downloaded from Yahoo Finance."""

from pathlib import Path

import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

TICKERS = ["AAPL", "NVDA", "ULVR.L"]


def raw_path(ticker: str) -> Path:
    """Return the path of the raw CSV file for a ticker."""
    return RAW_DIR / f"{ticker.replace('.', '_')}.csv"


def load_prices(ticker: str) -> pd.DataFrame:
    """Load the daily prices for one ticker, indexed by date."""
    return pd.read_csv(raw_path(ticker), index_col="Date", parse_dates=True)
