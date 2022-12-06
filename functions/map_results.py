from Models.model_calculation_data import OrderDataModel
from Models.model_profit_calculation import ProfitModel
from Models.model_result import ResultModel


def map_results(first_order, second_order, third_order, fourth_order, execution_data: OrderDataModel,
                analysis_data: ProfitModel):
    expected_result = ResultModel()
    real_result = ResultModel()
    if analysis_data.from_btc:
        expected_result.first_symbol = execution_data.symbol_BTC_USD
        expected_result.first_price = execution_data.price_BTC_USD
        expected_result.second_symbol = execution_data.symbol_BTC_TOKEN
        expected_result.second_price = execution_data.price_BTC_TOKEN
        expected_result.third_symbol = execution_data.symbol_ETH_TOKEN
        expected_result.third_price = execution_data.price_ETH_TOKEN
        expected_result.fourth_symbol = execution_data.symbol_ETH_USD
        expected_result.fourth_price = execution_data.price_ETH_USD
    elif analysis_data.from_eth:
        expected_result.first_symbol = execution_data.symbol_ETH_USD
        expected_result.first_price = execution_data.price_ETH_USD
        expected_result.second_symbol = execution_data.symbol_ETH_TOKEN
        expected_result.second_price = execution_data.price_ETH_TOKEN
        expected_result.third_symbol = execution_data.symbol_BTC_TOKEN
        expected_result.third_price = execution_data.price_BTC_TOKEN
        expected_result.fourth_symbol = execution_data.symbol_BTC_USD
        expected_result.fourth_price = execution_data.price_BTC_USD

    real_result.first_symbol = first_order["symbol"]
    real_result.first_price = float(first_order["fills"][0]["price"])
    real_result.second_symbol = second_order["symbol"]
    real_result.second_price = float(second_order["fills"][0]["price"])
    real_result.third_symbol = third_order["symbol"]
    real_result.third_price = float(third_order["fills"][0]["price"])
    real_result.fourth_symbol = fourth_order["symbol"]
    real_result.fourth_price = float(fourth_order["fills"][0]["price"])

    return expected_result, real_result


def print_results(expected_result: ResultModel, real_result: ResultModel):
    print(expected_result.first_symbol, expected_result.first_price, "->",
          expected_result.second_symbol, expected_result.second_price, "->",
          expected_result.third_symbol, expected_result.third_price, "->",
          expected_result.fourth_symbol, expected_result.fourth_price,)
    print(real_result.first_symbol, real_result.first_price, "->",
          real_result.second_symbol, real_result.second_price, "->",
          real_result.third_symbol, real_result.third_price, "->",
          real_result.fourth_symbol, real_result.fourth_price, )
