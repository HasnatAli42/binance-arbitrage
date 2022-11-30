import time

from Models.model_get_ticker import get_ticker_mapper
from binance_dir.client import client
from functions.calculate_arbitrage import remove_uncommon_pairs, calculate_arbitrage_data, calculate_arbitrage
from functions.sort_calculations import sort_calculated_data
from settings.settings import Dollar


def arbitrage():
    while True:

        total_tickers = []
        # Get Data
        try:
            total_tickers = client.get_ticker()
        except Exception as e:
            print("Api Exception ", e)

        # Reduce Data
        total_tickers = get_ticker_mapper(response=total_tickers)
        total_tickers, pairs_BTC, pairs_ETH, pairs_USD = remove_uncommon_pairs(required_pairs=total_tickers)

        # Perform Calculation
        raw_data = calculate_arbitrage_data(pairs_BTC=pairs_BTC, pairs_ETH=pairs_ETH,
                                            pairs_USD=pairs_USD, USD_Provided=Dollar)
        processed_data = calculate_arbitrage(raw_data=raw_data)

        # Sort Calculated Data
        sorted_data = sort_calculated_data(processed_data=processed_data)
        index = 0
        for data in sorted_data:
            print(index, ".Symbol", data.symbol, "Final USD =", data.net_increase_percent)
            index += 1

        time.sleep(2)
