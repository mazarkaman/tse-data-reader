from tesreader.ticker_base import TickerBase
from collections import namedtuple
import unicodedata as ud

class Ticker(TickerBase):
    def info(self):
        """returns namedtuple about ticker.\n
        attributes are: isin, code, company_en_name, company_isin,company_code, company_fa_name, fa_long_name, market, ticker, industry, industry_code, sub_industry, sub_industry_code, board_code
        """
        template = namedtuple('info', ["isin", "code", "company_en_name", "company_isin"
            , "company_code", "company_fa_name", "fa_long_name"
            , "market", "ticker", "industry", "industry_code"
            , "sub_industry", "sub_industry_code", "board_code"])

        info = self._get_info()

        return template(
            info["isin"], info["code"], info["company_en_name"], info["company_isin"]
            , info["company_code"], ud.normalize('NFC', info["company_fa_name"])
            , ud.normalize('NFC',info["fa_long_name"]), info["market"]
            , info["ticker"], info["industry"], info["industry_code"]
            , ud.normalize('NFC',info["sub_industry"]), info["sub_industry_code"], info["board_code"])

    def history(self, start_date: str = None, end_date: str = None, columns=None):
        """returns price history of specified ticker
        start_date and end_date are based on persian date for example:\n
        cols = ("max_price", "min_price", "close_price", "last_price", "first_price",
                "value", "trade_volume")
        ticker.history(start_date='1390-1-1', end_date='1398-9-1', columns=cols)
        """
        history = self._get_history(start_date, end_date)
        if columns:
            history = history.iloc[:, history.columns.isin(columns)]
        return history
