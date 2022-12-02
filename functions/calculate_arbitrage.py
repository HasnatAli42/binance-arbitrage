import string

from Models.model_calculation_data import OrderDataModel
from Models.model_profit_calculation import ProfitModel
from functions.calculate_percentage import calculate_percentages
from functions.price_conversions import convert_usd_to_btc, convert_btc_to_token, convert_token_to_eth, \
    convert_eth_to_usd, convert_btc_to_usd


def calculate_arbitrage(raw_data: list[OrderDataModel]):
    calculated_results = []
    # index = 0
    for data in raw_data:
        # if index != 100:
        calculate_obj = ProfitModel()
        calculate_obj.symbol = data.symbol_BTC_TOKEN
        calculate_obj.current_USD = float(data.initial_USD)
        calculate_obj.initial_USD = float(data.initial_USD)
        # print_calc(statement="Values Before Calculation", calculate_obj=calculate_obj)
        # Convert USD To BTC
        calculate_obj.current_USD, calculate_obj.current_BTC = convert_usd_to_btc(USD_used=data.initial_USD,
                                                                                  price=data.price_BTC_USD)
        # print_calc(statement="Convert USD To BTC", calculate_obj=calculate_obj)
        # Convert BTC To TOKEN
        calculate_obj.current_BTC, calculate_obj.current_TOKEN = convert_btc_to_token(
            BTC_used=calculate_obj.current_BTC
            , price=data.price_BTC_TOKEN)
        # print_calc(statement="Convert BTC To TOKEN", calculate_obj=calculate_obj)
        # Convert TOKEN to ETH
        calculate_obj.current_ETH, calculate_obj.current_TOKEN = convert_token_to_eth(TOKEN_used=
                                                                                      calculate_obj.current_TOKEN
                                                                                      , price=data.price_ETH_TOKEN)
        # print_calc(statement="Convert TOKEN to ETH", calculate_obj=calculate_obj)
        # Convert ETH to USD
        calculate_obj.current_USD, calculate_obj.current_ETH = convert_eth_to_usd(ETH_used=calculate_obj.current_ETH
                                                                                  ,
                                                                                  USD_avail=calculate_obj.current_USD
                                                                                  , price=data.price_ETH_USD)
        # print_calc(statement="Convert ETH to USD", calculate_obj=calculate_obj)
        # Convert Remaining BTC to USD
        calculate_obj.current_USD, calculate_obj.current_BTC = convert_btc_to_usd(BTC_avail=
                                                                                  calculate_obj.current_BTC,
                                                                                  USD_avail=
                                                                                  calculate_obj.current_USD,
                                                                                  price=data.price_BTC_USD)
        # print_calc(statement="Convert Remaining BTC to USD", calculate_obj=calculate_obj)
        calculate_obj.final_USD = calculate_obj.current_USD
        calculate_obj.gross_increase_USD, calculate_obj.net_increase_USD, \
        calculate_obj.gross_increase_percent, calculate_obj.net_increase_percent = calculate_percentages(
            initial=calculate_obj.initial_USD, final=calculate_obj.final_USD)
        calculated_results.append(calculate_obj)
        # index += 1
    return calculated_results


def calculate_arbitrage_data(pairs_BTC, pairs_ETH, pairs_USD, USD_Provided):
    calculated_results = []
    for pair in pairs_BTC:
        calculate_obj = OrderDataModel()
        calculate_obj.symbol_BTC_TOKEN = pair.symbol
        calculate_obj.price_BTC_TOKEN = float(pair.lastPrice)
        for stable_pair in pairs_USD:
            if stable_pair.symbol == "BTCBUSD":
                calculate_obj.symbol_BTC_USD = stable_pair.symbol
                calculate_obj.price_BTC_USD = float(stable_pair.lastPrice)
            elif stable_pair.symbol == "ETHBUSD":
                calculate_obj.symbol_ETH_USD = stable_pair.symbol
                calculate_obj.price_ETH_USD = float(stable_pair.lastPrice)
            elif stable_pair.symbol == "ETHBTC":
                calculate_obj.symbol_ETH_BTC = stable_pair.symbol
                calculate_obj.price_ETH_BTC = float(stable_pair.lastPrice)
        for alt_pair in pairs_ETH:
            if pair.symbol[0:-3] == alt_pair.symbol[0:-3]:
                calculate_obj.symbol_ETH_TOKEN = alt_pair.symbol
                calculate_obj.price_ETH_TOKEN = float(alt_pair.lastPrice)
        calculate_obj.initial_USD = float(USD_Provided)
        if calculate_obj.price_BTC_TOKEN != 0 and calculate_obj.price_ETH_TOKEN != 0:
            calculated_results.append(calculate_obj)
    return calculated_results


def remove_uncommon_pairs(required_pairs: list):
    reduced_pairs = []
    pairs_BTC = []
    pairs_ETH = []
    pairs_USD = []

    # Remove Uncommon Pairs
    for pair in required_pairs:
        if pair.symbol == "ETHBTC" or pair.symbol == "ETHBUSD" or pair.symbol == "BTCBUSD":
            reduced_pairs.append(pair)
            pairs_USD.append(pair)
        elif pair.symbol[-3:] == "BTC":
            for other_pair in required_pairs:
                if other_pair.symbol == pair.symbol[0:-3] + "ETH":
                    reduced_pairs.append(pair)
                    pairs_BTC.append(pair)
        elif pair.symbol[-3:] == "ETH":
            for other_pair in required_pairs:
                if other_pair.symbol == pair.symbol[0:-3] + "BTC":
                    reduced_pairs.append(pair)
                    pairs_ETH.append(pair)
    return reduced_pairs, pairs_BTC, pairs_ETH, pairs_USD


def print_calc(statement: string, calculate_obj: ProfitModel):
    print(statement)
    print("USD = " + str(calculate_obj.current_USD) + " BTC = " + str(calculate_obj.current_BTC)
          + " TOKEN = " + str(calculate_obj.current_TOKEN) + " ETH = " + str(calculate_obj.current_ETH))
