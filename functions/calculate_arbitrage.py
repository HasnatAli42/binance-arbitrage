from Models.model_calculation_data import CalculationDataModel
from Models.model_profit_calculation import ProfitModel
from functions.price_conversions import convert_usd_to_btc, convert_btc_to_token


def calculate_arbitrage(raw_data: list[CalculationDataModel]):
    calculated_results = []
    for data in raw_data:
        calculate_obj = ProfitModel()
        calculate_obj.symbol = data.symbol_BTC_TOKEN
        calculate_obj.initial_USD = float(data.initial_USD)

        # Convert USD To BTC
        calculate_obj.current_USD, calculate_obj.current_BTC = convert_usd_to_btc(USD_used=data.initial_USD,
                                                                                  price=data.price_BTC_USD)
        print("currentUSD=", calculate_obj.current_USD, "currentBTC=", calculate_obj.current_BTC)

        # Convert BTC To TOKEN
        calculate_obj.current_BTC, calculate_obj.current_TOKEN = convert_btc_to_token(BTC_used=calculate_obj.current_BTC,
                                                                                      price=data.price_BTC_TOKEN)
        print(data.price_BTC_TOKEN, "currentToken=", calculate_obj.current_TOKEN, "currentBTC=", calculate_obj.current_BTC)

    #     print("Sym=", data.symbol_BTC_USD, "Price=", data.price_BTC_USD,
    #           "Sym=", data.symbol_BTC_TOKEN, "Price=", data.price_BTC_TOKEN,
    #           "Sym=", data.symbol_ETH_TOKEN, "Price=", data.price_ETH_TOKEN,
    #           "Sym=", data.symbol_ETH_BTC, "Price=", data.price_ETH_BTC,
    #           "Sym=", data.symbol_ETH_USD, "Price=", data.price_ETH_USD, )
    # print(len(raw_data))


def calculate_arbitrage_data(pairs_BTC, pairs_ETH, pairs_USD, USD_Provided):
    calculated_results = []
    for pair in pairs_BTC:
        calculate_obj = CalculationDataModel()
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
