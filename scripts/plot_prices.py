"""Plot the three stocks' dividend-adjusted performance since 2024."""

from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

from prices import TICKERS, load_prices

ROOT_DIR = Path(__file__).resolve().parents[1]
OUTPUT_PATH = ROOT_DIR / "figures" / "stock_prices_since_2024.png"
START_DATE = "2024-01-01"


def main() -> None:
    fig, ax = plt.subplots(figsize=(12, 6))

    for ticker in TICKERS:
        prices = load_prices(ticker)["Adj Close"]
        prices = prices.loc[prices.index >= START_DATE]
        performance = (prices / prices.iloc[0] - 1) * 100
        ax.plot(performance.index, performance, label=ticker, linewidth=1.8)

    ax.set_title("Stock price performance since 2024")
    ax.set_xlabel("Date")
    ax.set_ylabel("Change from first trading day (%)")
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.grid(True, alpha=0.3)
    ax.legend(title="Ticker")
    fig.tight_layout()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT_PATH, dpi=160)
    plt.close(fig)
    print(f"Saved chart to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
