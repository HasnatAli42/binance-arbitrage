class MarketOrderModel:
    def __init__(self):
        self.symbol = ""
        self.orderId = 0
        self.orderListId = -1
        self.clientOrderId = ""
        self.transactTime = 0
        self.price = 0
        self.origQty = ""
        self.executedQty = ""
        self.cummulativeQuoteQty = ""
        self.status = ""
        self.timeInForce = "GTC"
        self.type = "MARKET"
        self.side = ""
        self.fills = list[Fills]


class Fills:
    def __init__(self):
        self.price = ""
        self.qty = 0
        self.commission = ""
        self.commissionAsset = ""
        self.tradeId = 0
        self.price = 0
