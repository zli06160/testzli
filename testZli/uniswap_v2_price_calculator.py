# constant pair fee rate at 0.30%
V2FEES = 0.003

class UniswapV2PriceCalculator:
    def __init__(self, name: str = "default V2 Price Calculator"):
        self.name = name

    def calculatePrice(self, a: int, b: int, c: int, d: int):
        return (a + b) / (c + d)
