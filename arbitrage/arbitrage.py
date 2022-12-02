import time
import json

from Models.model_calculation_data import OrderDataModel
from Models.model_get_exchange_info import ExchangeInfoModel
from Models.model_get_ticker import get_ticker_mapper
from Models.model_order_market import MarketOrderModel
from Models.model_profit_calculation import ProfitModel
from binance_dir.client import client
from functions.calculate_arbitrage import remove_uncommon_pairs, calculate_arbitrage_data, calculate_arbitrage
from functions.orders import place_order_usd_to_btc, place_order_btc_to_token
from functions.required_data import required_data
from functions.sort_calculations import sort_calculated_data
from settings.settings import Dollar


def arbitrage():
    while True:
        analysis_data = ProfitModel()
        order_execution_data = OrderDataModel()
        first_order = MarketOrderModel()
        second_order = MarketOrderModel()
        symbol_info = ExchangeInfoModel()
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
        print("FROM BTC Symbol", sorted_data[0].symbol, "Final USD =", sorted_data[0].net_increase_percent)
        print("FROM ETH Symbol", sorted_data[-1].symbol, "Final USD =", sorted_data[-1].net_increase_percent)
        analysis_data, order_execution_data = required_data(analysis_data=sorted_data, execution_data=raw_data)
        print("Required Analysiss Data", json.dumps(analysis_data.__dict__))
        print("Required Execution Data", json.dumps(order_execution_data.__dict__))
        print(client.get_symbol_info(symbol="JASMYBTC"))
        first_order = place_order_usd_to_btc(analysis_data=analysis_data, order_data=order_execution_data)
        print(first_order)
        second_order = place_order_btc_to_token(analysis_data=analysis_data,
                                                order_data=order_execution_data, pre_order=first_order)
        print(second_order)

        time.sleep(2)
