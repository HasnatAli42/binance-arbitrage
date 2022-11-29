from settings.settings import decimals_btc, decimals_usd


def convert_usd_to_btc(USD_used: float, price: float):
    raw_btc = USD_used / price
    processed_btc = float(int(raw_btc * decimals_btc)) / decimals_btc
    remaining_usd = float(float(raw_btc * decimals_btc) - float(int(raw_btc * decimals_btc))) / decimals_btc
    remaining_usd = (int(remaining_usd * decimals_usd)) / decimals_usd
    return remaining_usd, processed_btc


def convert_btc_to_token(BTC_used: float, price: float):
    token, btc = divmod(BTC_used, price)
    btc = float(int(btc * decimals_btc)) / decimals_btc
    return float(btc), float(token)


def convert_token_to_eth(TOKEN_used: float, price: float):
    eth = TOKEN_used * price
    return float(eth), float(0)


def convert_eth_to_usd(ETH_used: float, USD_avail: float, price: float):
    usd = USD_avail + (ETH_used * price)
    return float(usd), float(0)


def convert_btc_to_usd(BTC_avail: float, USD_avail: float, price: float):
    usd = USD_avail + (BTC_avail * price)
    return float(usd), float(0)
