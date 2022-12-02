class ExchangeInfoModel:
    def __init__(self):
        self.symbol = ""
        self.status = "TRADING"
        self.baseAsset = "BTC"
        self.baseAssetPrecision = 0
        self.quoteAsset = "BUSD"
        self.quotePrecision = 0
        self.quoteAssetPrecision = 0
        self.baseCommissionPrecision = 0
        self.quoteCommissionPrecision = 0
        self.orderTypes = []
        self.icebergAllowed = True
        self.ocoAllowed = True
        self.quoteOrderQtyMarketAllowed = True
        self.allowTrailingStop = True
        self.cancelReplaceAllowed = True
        self.isSpotTradingAllowed = True
        self.isMarginTradingAllowed = True
        self.filters = list[Filters]
        self.permissions = []


class Filters:
    def __init__(self):
        self.filterType = ""
        self.minPrice = ""
        self.maxPrice = ""
        self.tickSize = ""
        self.multiplierUp = ""
        self.multiplierDown = ""
        self.avgPriceMins = 0
        self.minQty = ""
        self.maxQty = ""
        self.stepSize = ""
        self.minNotional = ""
        self.multiplierDown = ""
        self.applyToMarket = ""
        self.limit = 0
        self.maxQty = ""
        self.stepSize = ""
        self.minTrailingAboveDelta = 0
        self.maxTrailingAboveDelta = 0
        self.minTrailingBelowDelta = 0
        self.maxTrailingBelowDelta = 0
        self.maxNumOrders = 0
        self.maxNumAlgoOrders = 0
