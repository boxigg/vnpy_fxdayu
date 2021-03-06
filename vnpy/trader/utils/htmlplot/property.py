

class Property(object):

    def __init__(self, **kwargs):
        self.background = "#FFFFFF"
        self.candle_hl = dict()
        self.up_candle = dict()
        self.down_candle = dict()
        self.long_trade_line = dict()
        self.short_trade_line = dict()
        self.long_trade_tri = dict()
        self.short_trade_tri = dict()
        self.trade_close_tri = dict()
        for key, value in kwargs.items():
            setattr(self, key, value)

# BigFishProperty -----------------------------------------------------

BF_LONG = "#208C13"
BF_SHORT = "#D32C25"
BF_CLOSE = "#F9D749"
BF_KLINE = "#4DB3C7"
BF_BG = "#FFFFFF"

BigFishProperty = Property(
    background=BF_BG,
    candle_hl=dict(
        color=BF_KLINE
    ),
    up_candle=dict(
        fill_color=BF_BG, 
        line_color=BF_KLINE
    ),
    down_candle = dict(
        fill_color=BF_KLINE, 
        line_color=BF_KLINE
    ),
    long_trade_line=dict(
        color=BF_LONG
    ),
    short_trade_line=dict(
        color=BF_SHORT
    ),
    long_trade_tri=dict(
        line_color="black", 
        fill_color=BF_LONG
    ),
    short_trade_tri=dict(
        line_color="black", 
        fill_color=BF_SHORT
    ),
    trade_close_tri=dict(
        line_color="black", 
        fill_color=BF_CLOSE
    )
)


# BigFishProperty -----------------------------------------------------


# MT4Property ---------------------------------------------------------

MT4_LONG = "blue"
MT4_SHORT = "red"
MT4_CLOSE = "gold"
MT4_KLINE = "#00FF00"
MT4_BG = "#000000"


MT4Property = Property(
    background=MT4_BG,
    candle_hl=dict(
        color=MT4_KLINE
    ),
    up_candle=dict(
        fill_color=MT4_BG, 
        line_color=MT4_KLINE
    ),
    down_candle = dict(
        fill_color=MT4_KLINE, 
        line_color=MT4_KLINE
    ),
    long_trade_line=dict(
        color=MT4_LONG
    ),
    short_trade_line=dict(
        color=MT4_SHORT
    ),
    long_trade_tri=dict(
        line_color="#FFFFFF", 
        fill_color=MT4_LONG
    ),
    short_trade_tri=dict(
        line_color="#FFFFFF", 
        fill_color=MT4_SHORT
    ),
    trade_close_tri=dict(
        line_color="#FFFFFF", 
        fill_color=MT4_CLOSE
    )
)


# MT4Property ---------------------------------------------------------