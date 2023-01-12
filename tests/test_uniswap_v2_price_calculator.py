import unittest

from testzli.uniswap_v2_price_calculator import V2FEES, PRICE_LIMIt, UniswapV2PriceCalculator


class MyTestCase(unittest.TestCase):
    """
    Here are the necessary unit tests for the UniSwapV2 Price Calculator.
    They should cover all types of inputs params, and be checked with manually calculated reference results like belows.
    """

    def test_fee_rate(self):
        self.assertEqual(0.003, V2FEES)

    def test_price_limit(self):
        self.assertEqual(100000, PRICE_LIMIt)

    def test_with_ones(self):
        calculator = UniswapV2PriceCalculator()
        result = calculator.calculate_price(1, 1, 1)
        self.assertEqual(1, result)

    def test_with_twos(self):
        calculator = UniswapV2PriceCalculator()
        result = calculator.calculate_price(2, 2, 2)
        self.assertEqual(2, result)

    def test_with_exceeded_result(self):
        calculator = UniswapV2PriceCalculator()
        result = calculator.calculate_price(10000, 5000, 200)
        # it should return 0, 10000*50000/200=2500000>PRICE_LIMIT
        self.assertEqual(0, result)

    def test_with_randoms1(self):
        calculator = UniswapV2PriceCalculator()
        result = calculator.calculate_price(2, 3.5, 8)
        self.assertEqual(0.875, result)

    def test_with_randoms2(self):
        calculator = UniswapV2PriceCalculator()
        result = calculator.calculate_price(1000, 5000, 2000)
        self.assertEqual(2500, result)


if __name__ == '__main__':
    unittest.main()
