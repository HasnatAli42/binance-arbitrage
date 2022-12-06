from Models.model_calculation_data import OrderDataModel
from Models.model_order_market import MarketOrderModel
from Models.model_profit_calculation import ProfitModel
from binance_dir.client import client
from settings.settings import decimals_btc, btc_to_usd_decimals, eth_to_usd_decimals


def place_order_usd_to_btc(analysis_data: ProfitModel, order_data: OrderDataModel):
    order = MarketOrderModel()
    if analysis_data.from_btc:
        # btc_qty = float(
        #     int((order_data.initial_USD / order_data.price_BTC_USD) * btc_to_usd_decimals)) / btc_to_usd_decimals
        order = client.order_market_buy(symbol=order_data.symbol_BTC_USD, quoteOrderQty=order_data.initial_USD)
    elif analysis_data.from_eth:
        # eth_qty = float(
        #     int((order_data.initial_USD / order_data.price_ETH_USD) * eth_to_usd_decimals)) / eth_to_usd_decimals
        order = client.order_market_buy(symbol=order_data.symbol_ETH_USD, quoteOrderQty=order_data.initial_USD)
    return order


def place_order_btc_to_token(analysis_data: ProfitModel, order_data: OrderDataModel, pre_order):
    order = MarketOrderModel()
    if analysis_data.from_btc:
        # token_qty = int(float(pre_order.executedQty) / order_data.price_BTC_TOKEN)
        order = client.order_market_buy(symbol=order_data.symbol_BTC_TOKEN, quoteOrderQty=float(pre_order["executedQty"]))
    elif analysis_data.from_eth:
        # token_qty = int(float(pre_order.executedQty) / order_data.price_ETH_TOKEN)
        order = client.order_market_buy(symbol=order_data.symbol_ETH_TOKEN, quoteOrderQty=float(pre_order["executedQty"]))
    return order


def place_order_token_to_btc(analysis_data: ProfitModel, order_data: OrderDataModel, pre_order):
    order = MarketOrderModel()
    if analysis_data.from_btc:
        # eth_qty = float(int(float(float(pre_order.executedQty) *
        # order_data.price_ETH_TOKEN)*decimals_btc))/decimals_btc
        order = client.order_market_sell(symbol=order_data.symbol_ETH_TOKEN, quantity=float(pre_order["executedQty"]))
    elif analysis_data.from_eth:
        # btc_qty = float(int(float(float(pre_order.executedQty) *
        # order_data.price_BTC_TOKEN)*decimals_btc))/decimals_btc
        order = client.order_market_sell(symbol=order_data.symbol_BTC_TOKEN, quantity=float(pre_order["executedQty"]))
    return order


def place_order_btc_to_usd(analysis_data: ProfitModel, order_data: OrderDataModel, pre_order):
    order = MarketOrderModel()
    if analysis_data.from_btc:
        # usd_qty = float(float(pre_order.executedQty) * order_data.price_ETH_USD)
        order = client.order_market_sell(symbol=order_data.symbol_ETH_USD, quoteOrderQty=float(order_data.initial_USD))
    elif analysis_data.from_eth:
        # usd_qty = float(float(pre_order.executedQty) * order_data.price_BTC_USD)
        order = client.order_market_sell(symbol=order_data.symbol_BTC_USD, quoteOrderQty=float(order_data.initial_USD))
    return order
