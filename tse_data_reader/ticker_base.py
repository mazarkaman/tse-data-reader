import datetime
from io import StringIO
import pandas as pd
import jdatetime
import requests
from bs4 import BeautifulSoup

from tse_data_reader.market_base import MarketBase


class TickerBase(object):
    def __init__(self, ticker_name: str):
        self._market = MarketBase()
        self.ticker_name = ticker_name
        self.ticker_id = self.get_id()

        self._info_url = MarketBase.base_url + \
                         "/Loader.aspx?Partree=15131M&i={}".format(self.ticker_id)

        self._history_url = MarketBase.base_url + \
                            "/tsev2/data/InstTradeHistory.aspx?i={}&Top=999999&A=1".format(self.ticker_id)

        self._info = None
        self._history = None

    def _get_info(self):
        req = requests.request("GET", self._info_url, timeout=400)
        data = BeautifulSoup(req.text, features="html.parser")
        ret = {}
        ret.update({"isin": data.select(".table1 > tbody > tr:nth-child(1) > td:nth-child(2)")[0].text.strip()})
        ret.update({"code": data.select(".table1 > tbody > tr:nth-child(2) > td:nth-child(2)")[0].text.strip()})
        ret.update(
            {"company_en_name": data.select(".table1 > tbody > tr:nth-child(3) > td:nth-child(2)")[0].text.strip()})
        ret.update({"company_isin": data.select(".table1 > tbody > tr:nth-child(8) > td:nth-child(2)")[0].text.strip()})
        ret.update({"company_code": data.select(".table1 > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text.strip()})
        ret.update(
            {"company_fa_name": data.select(".table1 > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text.strip()})
        ret.update({"fa_long_name": data.select(".table1 > tbody > tr:nth-child(7) > td:nth-child(2)")[0].text.strip()})
        ret.update({"market": data.select(".table1 > tbody > tr:nth-child(9) > td:nth-child(2)")[0].text.strip()})
        ret.update({"ticker": data.select(".table1 > tbody > tr:nth-child(6) > td:nth-child(2)")[0].text.strip()})
        ret.update({"industry": data.select(".table1 > tbody > tr:nth-child(12) > td:nth-child(2)")[0].text.strip()})
        ret.update(
            {"industry_code": data.select(".table1 > tbody > tr:nth-child(11) > td:nth-child(2)")[0].text.strip()})
        ret.update(
            {"sub_industry": data.select(".table1 > tbody > tr:nth-child(14) > td:nth-child(2)")[0].text.strip()})
        ret.update(
            {"sub_industry_code": data.select(".table1 > tbody > tr:nth-child(13) > td:nth-child(2)")[0].text.strip()})
        ret.update({"board_code": data.select(".table1 > tbody > tr:nth-child(10) > td:nth-child(2)")[0].text.strip()})
        return ret

    def _get_history(self, start_date: str = None, end_date: str = None):
        data = self._get_history_raw()
        data = StringIO(data)
        df = pd.read_csv(data, sep="@")

        df.columns = ["date", "max_price", "min_price", "close_price",
                      "last_price", "first_price", "yesterday_price",
                      "value", "trade_volume", "trade_count"]

        df["date"] = pd.DatetimeIndex(pd.to_datetime(df["date"], format="%Y%m%d"))
        df.set_index("date", inplace=True)
        df.sort_index(ascending=True, inplace=True)

        if start_date:
            start_date = jdatetime.datetime.strptime(start_date, '%Y-%m-%d').togregorian()
            df = df.loc[start_date:]

        if end_date:
            end_date = jdatetime.datetime.strptime(end_date, '%Y-%m-%d').togregorian()
        else:
            end_date = datetime.datetime.now()

        df = df.loc[:end_date]

        return df

    def get_id(self):
        board = self._market._get_board()
        _id = board.loc[self.ticker_name]["id"]
        return _id

    def _get_history_raw(self):
        req = requests.request("GET", self._history_url, timeout=40)
        data = req.text.replace(";", "\n")
        return data
