import unittest

from best_time_to_buy_and_sell_stock_leetcode_121.best_time_to_buy_and_sell_stock import (
    Solution,
)


class TestBestTimeToBuyAndSellStock(unittest.TestCase):
    def setUp(self) -> None:

        self.stock_profit = Solution()
        self.prices_1 = [7, 6, 4, 3, 1]
        self.prices_2 = [7, 1, 5, 3, 6, 4]

    def test_best_time_to_buy_and_sell_stock(self) -> None:

        self.assertEqual(self.stock_profit.max_profit(self.prices_1), 0)
        self.assertEqual(self.stock_profit.max_profit(self.prices_2), 5)
