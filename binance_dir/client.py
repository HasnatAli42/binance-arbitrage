from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

from settings.settings import api_key, secret_key

client = Client(api_key=api_key, api_secret=secret_key)
