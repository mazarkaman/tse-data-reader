from io import StringIO
import pandas as pd
import ast
import requests
import unicodedata as ud

from tse_data_reader.utils import normalize_persian_chars


class MarketBase(object):
    base_url = "http://cdn.tsetmc.com"

    def __init__(self):
        self._tickers_list_address = self.base_url + "/tsev2/data/MarketWatchInit.aspx?h=0&r=0"
        self._industries_address = self.base_url + "/tsev2/res/loader.aspx?t=g"

    def _get_board(self):
        try:
            tickers = requests.request("GET", self._tickers_list_address,
                                       timeout=400, stream=True)
            raw_data = tickers.text.split("@")[2]
            raw_data = raw_data.replace(";", "\n")
            data = pd.read_csv(StringIO(raw_data), sep=",")
            data.columns = ["id", "isin", "code", "fa_name", "un1",
                            "first_price", "last_price", "last_trade", "count",
                            "volume", "value", "min_price", "max_price", "y_price",
                            "eps", "base_volume", "un2", "bit_count", "industry_code",
                            "max_allowed_price", "min_allowed_price", "share_count", "type"]

            data['code'] = normalize_persian_chars(data['code'].str)
            data.set_index("code", inplace=True)
            return data
        except IndexError:
            raise IndexError("there is problem in getting data")

    def _get_industries(self):
        request = requests.get(self._industries_address)
        text = ud.normalize('NFC', request.text).replace("var Sectors=", "") \
            .replace("'", '"').replace('","', '":"').replace(";", "") \
            .replace("],[", ",").replace("[[", "{").replace("]]", "}")
        dic = dict(ast.literal_eval(text))
        ret = {v: k for k, v in dic.items()}
        return ret
