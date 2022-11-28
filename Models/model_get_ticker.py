
def get_ticker_mapper(response):
    mapped_array = []
    for obj in response:
        if obj["symbol"].rfind("BTC") != -1 or obj["symbol"].rfind("ETH") != -1:
            mapped_array.append(GetTickerModel(obj=obj))
    return mapped_array


class GetTickerModel:
    def __init__(self, obj):
        self.symbol = obj["symbol"]
        self.priceChange = obj["priceChange"]
        self.priceChangePercent = obj["priceChangePercent"]
        self.weightedAvgPrice = obj["weightedAvgPrice"]
        self.prevClosePrice = obj["prevClosePrice"]
        self.lastPrice = obj["lastPrice"]
        self.lastQty = obj["lastQty"]
        self.bidPrice = obj["bidPrice"]
        self.bidQty = obj["bidQty"]
        self.askPrice = obj["askPrice"]
        self.askQty = obj["askQty"]
        self.openPrice = obj["openPrice"]
        self.highPrice = obj["highPrice"]
        self.lowPrice = obj["lowPrice"]
        self.volume = obj["volume"]
        self.quoteVolume = obj["quoteVolume"]
        self.openTime = obj["openTime"]
        self.closeTime = obj["closeTime"]
        self.firstId = obj["firstId"]
        self.lastId = obj["lastId"]
        self.count = obj["count"]

