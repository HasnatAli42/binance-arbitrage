from settings.settings import decimals


def convert_usd_to_btc(USD_used: float, price: float):
    raw_btc = USD_used / price
    processed_btc = float(int(raw_btc * decimals))/decimals
    remaining_usd = float((raw_btc * decimals) - int(raw_btc * decimals))/decimals
    return remaining_usd, processed_btc


def convert_btc_to_token(BTC_used: float, price: float):
    token, btc = divmod(BTC_used, price)
    return float(token), float(btc)

