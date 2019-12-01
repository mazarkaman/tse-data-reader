import unittest
from tesreader.ticker import Ticker


class TestData(unittest.TestCase):
    def setUp(self):
        self.ticker = Ticker('فخوز')

    def test_ticker_info(self):
        info = self.ticker.info()
        self.assertIsNotNone(info.isin)
        self.assertEqual(info.isin, "IRO1FKHZ0001")
        self.assertIsNotNone(info.code)
        self.assertIsNotNone(info.company_en_name)
        self.assertIsNotNone(info.company_isin)
        self.assertIsNotNone(info.company_code)
        self.assertIsNotNone(info.company_fa_name)
        self.assertIsNotNone(info.fa_long_name)
        self.assertIsNotNone(info.market)
        self.assertIsNotNone(info.ticker)
        self.assertIsNotNone(info.industry)
        self.assertIsNotNone(info.industry_code)
        self.assertIsNotNone(info.sub_industry)
        self.assertIsNotNone(info.sub_industry_code)
        self.assertIsNotNone(info.board_code)

    def test_history(self):
        cols = ("max_price", "min_price", "close_price", "last_price", "first_price",
                "value")

        history = self.ticker.history(start_date='1390-1-1', end_date='1398-9-1', columns=cols)
        self.assertListEqual(list(history.columns.values), list(cols))
        self.assertGreater(len(history.index), 0)

    def test_history_without_parameters(self):
        history = self.ticker.history()
        self.assertGreater(len(history.index), 0)

