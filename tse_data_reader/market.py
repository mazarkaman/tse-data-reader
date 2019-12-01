from tse_data_reader.market_base import MarketBase


class Market(MarketBase):
    def get_main_board(self):
        return self._get_board()

    def get_industries(self):
        return self._get_industries()
