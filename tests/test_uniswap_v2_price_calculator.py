import unittest

from testZli.uniswap_v2_price_calculator import UniswapV2PriceCalculator


class MyTestCase(unittest.TestCase):
    """
    Here are the necessary units tests for the  UniSwapV2 Price Calculator.
    They should cover all types of inputs params, and be checked with manually calculated reference results.
    """
    def test_with_ones(self):
        calculator = UniswapV2PriceCalculator()
        result = calculator.calculate_price(1, 1, 1, 1)
        self.assertEqual(1, result)  # add assertion here

    def test_with_twos(self):
        calculator = UniswapV2PriceCalculator()
        result = calculator.calculate_price(2.0, 2, 2, 2)
        self.assertEqual(1, result)  # add assertion here

    def test_with_randoms(self):
        calculator = UniswapV2PriceCalculator()
        result = calculator.calculate_price(2.0, 3.5, 8, 10)
        self.assertEqual(0.3055555555555556, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()

