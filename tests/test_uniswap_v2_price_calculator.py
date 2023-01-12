import unittest

from testZli.uniswap_v2_price_calculator import UniswapV2PriceCalculator


class MyTestCase(unittest.TestCase):
    """
    Here are the necessary units tests for the  UniswapV2 Price Calculator.
    They should cover all types of inputs params, and be checked with manually calculated reference results.
    """
    def test_with_ones(self):
        calculator = UniswapV2PriceCalculator()
        result = calculator.calculatePrice(1, 1, 1, 1)
        self.assertEqual(1, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
