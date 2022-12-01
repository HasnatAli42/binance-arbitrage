from Models.model_calculation_data import CalculationDataModel
from Models.model_profit_calculation import ProfitModel


def required_data(analysis_data: list[ProfitModel], execution_data: list[CalculationDataModel]):
    if abs(analysis_data[0].net_increase_percent) > abs(analysis_data[-1].net_increase_percent):
        analysis_data = analysis_data[0]
        analysis_data.from_btc = True
    else:
        analysis_data = analysis_data[-1]
        analysis_data.from_eth = True

    for data in execution_data:
        if analysis_data.symbol == data.symbol_BTC_TOKEN or analysis_data.symbol == data.symbol_ETH_TOKEN:
            order_data = data
    return analysis_data, order_data
