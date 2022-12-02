from Models.model_calculation_data import CalculationDataModel
from Models.model_profit_calculation import ProfitModel
from binance_dir.client import client
from settings.settings import decimals_btc, btc_to_usd_decimals, eth_to_usd_decimals


def place_order_usd_to_btc(analysis_data: ProfitModel, order_data: CalculationDataModel):
    order = ""
    if analysis_data.from_btc:
        btc_qty = float(int((order_data.initial_USD / order_data.price_BTC_USD) * btc_to_usd_decimals))/btc_to_usd_decimals
        print(str(btc_qty))
        order = client.order_market_buy(symbol=order_data.symbol_BTC_USD, quantity=btc_qty)
    elif analysis_data.from_eth:
        eth_qty = float(int((order_data.initial_USD / order_data.price_ETH_USD) * eth_to_usd_decimals)) / eth_to_usd_decimals
        order = client.order_market_buy(symbol=order_data.symbol_ETH_USD, quantity=eth_qty)
    return order
