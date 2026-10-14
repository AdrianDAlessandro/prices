import hashlib

import pytest

from prices import TICKERS, load_prices
from prices.load import raw_path

# The raw files must never change. If you add a ticker, add its checksum here.
RAW_SHA256 = {
    "AAPL": "c48f08454582f773523ceea07b79778b028db976f5c5359b39d629b8c3e1d95c",
    "NVDA": "c0af140547ab4f00f62e339974c37ff1b601b20a20dc871df4221c07cbcdd47e",
    "ULVR.L": "05a997ad8a52c6844ac7103213aa7a1aaa3c09f71f6e145594ff9fc012547751",
}


@pytest.mark.parametrize("ticker", TICKERS)
def test_raw_data_unchanged(ticker: str) -> None:
    digest = hashlib.sha256(raw_path(ticker).read_bytes()).hexdigest()
    assert digest == RAW_SHA256[ticker], f"{raw_path(ticker).name} has been edited"


@pytest.mark.parametrize("ticker", TICKERS)
def test_load_prices_has_expected_columns(ticker: str) -> None:
    df = load_prices(ticker)
    assert list(df.columns) == ["Adj Close", "Close", "High", "Low", "Open", "Volume"]
    assert df.index.is_monotonic_increasing
