import time
import json

from Models.model_calculation_data import OrderDataModel
from Models.model_get_exchange_info import ExchangeInfoModel
from Models.model_get_ticker import get_ticker_mapper
from Models.model_order_market import MarketOrderModel
from Models.model_profit_calculation import ProfitModel
from Models.model_result import ResultModel
from binance_dir.client import client
from functions.calculate_arbitrage import remove_uncommon_pairs, calculate_arbitrage_data, calculate_arbitrage, \
    remove_low_priced_tokens
from functions.map_results import map_results, print_results
from functions.orders import place_order_usd_to_btc, place_order_btc_to_token, place_order_token_to_btc, \
    place_order_btc_to_usd
from functions.required_data import required_data
from functions.sort_calculations import sort_calculated_data
from settings.settings import Dollar, TIME_SLEEP


def arbitrage():
    while True:
        analysis_data = ProfitModel()
        order_execution_data = OrderDataModel()
        first_order = MarketOrderModel()
        second_order = MarketOrderModel()
        third_order = MarketOrderModel()
        fourth_order = MarketOrderModel()
        expected_result = ResultModel()
        real_result = ResultModel()
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
        # Remove Unwanted Data
        # raw_data = remove_low_priced_tokens(raw_data=raw_data)

        # Process Data
        processed_data = calculate_arbitrage(raw_data=raw_data)

        # Sort Calculated Data
        sorted_data = sort_calculated_data(processed_data=processed_data)
        print("FROM BTC Symbol", sorted_data[0].symbol, "Final USD =", sorted_data[0].net_increase_percent)
        print("FROM ETH Symbol", sorted_data[-1].symbol, "Final USD =", sorted_data[-1].net_increase_percent)
        analysis_data, order_execution_data = required_data(analysis_data=sorted_data, execution_data=raw_data)
        print("Required Analysiss Data", json.dumps(analysis_data.__dict__))
        print("Required Execution Data", json.dumps(order_execution_data.__dict__))
        if abs(analysis_data.net_increase_percent) > 3:
            first_order = place_order_usd_to_btc(analysis_data=analysis_data, order_data=order_execution_data)
            print("First Order:", first_order)
            second_order = place_order_btc_to_token(analysis_data=analysis_data,
                                                    order_data=order_execution_data, pre_order=first_order)
            print("Second Order:", second_order)
            third_order = place_order_token_to_btc(analysis_data=analysis_data,
                                                   order_data=order_execution_data, pre_order=second_order)
            print("Third Order:", third_order)
            fourth_order = place_order_btc_to_usd(analysis_data=analysis_data,
                                                  order_data=order_execution_data, pre_order=third_order)
            print("Fourth Order:", fourth_order)
            # Get Results
            expected_result, real_result = map_results(first_order=first_order, second_order=second_order,
                                                       third_order=third_order, fourth_order=fourth_order,
                                                       execution_data=order_execution_data,
                                                       analysis_data=analysis_data)
            print_results(expected_result=expected_result, real_result=real_result)
        else:
            print("Mark Value Not Achieved")
        time.sleep(TIME_SLEEP)
