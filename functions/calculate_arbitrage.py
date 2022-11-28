def remove_uncommon_pairs(required_pairs: list):
    reduced_pairs = []

    # Remove Uncommon Pairs
    for pair in required_pairs:
        if pair.symbol == "ETHBTC" or pair.symbol == "ETHBUSD" or pair.symbol == "BTCBUSD":
            reduced_pairs.append(pair)
        elif pair.symbol[-3:] == "BTC":
            for other_pair in required_pairs:
                if other_pair.symbol == pair.symbol[0:-3] + "ETH":
                    reduced_pairs.append(pair)
        elif pair.symbol[-3:] == "ETH":
            for other_pair in required_pairs:
                if other_pair.symbol == pair.symbol[0:-3] + "BTC":
                    reduced_pairs.append(pair)
    return reduced_pairs

