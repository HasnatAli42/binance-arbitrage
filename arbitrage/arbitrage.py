import time

from binance_dir.client import client


def arbitrage():
    while True:
        total_tickers = client.get_ticker()
        print("Arbitrage", len(total_tickers))
        for obj in total_tickers:
            if obj["symbol"] == "BTCBUSD":
                print("BTCBUSD = ", obj["lastPrice"])
        print("End")
        time.sleep(2)
