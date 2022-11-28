import time

from Models.model_get_ticker import get_ticker_mapper
from binance_dir.client import client
from functions.calculate_arbitrage import remove_uncommon_pairs


def arbitrage():
    while True:
        # Get Data
        total_tickers = client.get_ticker()
        print("Before Cleaning Arbitrage", len(total_tickers))

        # Reduce Data
        total_tickers = get_ticker_mapper(response=total_tickers)
        total_tickers = remove_uncommon_pairs(required_pairs=total_tickers)

        # Perform Calculation

        print("After Cleaning Arbitrage", len(total_tickers))
        time.sleep(2)
