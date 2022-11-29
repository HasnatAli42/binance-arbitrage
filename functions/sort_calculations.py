from Models.model_profit_calculation import ProfitModel


def sort_calculated_data(processed_data: list[ProfitModel]):
    processed_data.sort(key=lambda x: x.net_increase_percent, reverse=True)
    return processed_data

