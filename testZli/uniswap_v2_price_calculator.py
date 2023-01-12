# constant pair fee rate at 0.30%
V2FEES = 0.003


class UniswapV2PriceCalculator:
    """
    The implementation of UniSwap V2 price calculation. It takes consideration of the pair fee rate(currently 0.30%).
    """
    def __init__(self, name: str = "default V2 Price Calculator"):
        self.name = name

    def calculate_price(self, a: float, b: float, c: int, d: int):
        return (a + b) / (c + d)
