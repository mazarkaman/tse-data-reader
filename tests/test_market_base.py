import unittest

from tesreader.market_base import MarketBase


class TestMarketBase(unittest.TestCase):
    def setUp(self):
        self.base = MarketBase()

    def test_industries(self):
        self.base._get_industries()
