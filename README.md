
# TSE data reader
This package scraps data from Tehran's stock market website (tsetmc.com) so you can use this library in your analytical projects

## Installation

```sh
pip install --upgrade tse-data-reader
```

## Usage example

```python
>> from tse_data_reader.ticker import Ticker
>> tikcer = Ticker('فخوز')
>> tikcer.info()
info(isin='IRO1FKHZ0001', code='FKHZ1', company_en_name='Khouz. Steel', company_isin='IRO1FKHZ0003', company_code='FKHZ', company_fa_name='فولاد خوزستان', fa_long_name='فولاد  خوزستان', market='بازار اول (تابلوي اصلي) بورس', ticker='فخوز', industry='فلزات اساسي', industry_code='27', sub_industry='توليد آهن و فولاد پايه', sub_industry_code='2710', board_code='1')

>> hist = ticker.history(start_date='1390-1-1',end_date='1398-9-1')
>> hist.head()
>
            max_price  min_price  ...  trade_volume  trade_count
date                              ...                           
2011-03-26     8278.0     8044.0  ...        275124           32
2011-03-27     8356.0     8349.0  ...        115324           47
2011-03-28     8389.0     8066.0  ...        122006           20
2011-03-29     8420.0     8350.0  ...       1495482           86
2011-03-30     8749.0     8252.0  ...        361047           50
...               ...        ...  ...           ...          ...
2019-11-16     8899.0     8650.0  ...       1197713          368
2019-11-17     9199.0     8400.0  ...       4703375          646
2019-11-18     8885.0     8800.0  ...       1115825          275
2019-11-19     8996.0     8759.0  ...        652271          261
2019-11-20     8945.0     8630.0  ...       1316684          546

[2097 rows x 9 columns]
```

## Release History
* 0.1.0
    * ticker info()
    * ticker history()
    * market get_industries()
    * market get_main_board()
* 0.1.1
    * fixed dependencies issue

## Meta

Mohammad Sadegh Azarkaman –  azarkaman.net@gmail.com

**THIS PROJECT IS NOT FOR COMMERCIAL USE**
**DONT ABUSE THIS LIBRARY, FOR EXAMPLE DON'T CALL FUNCTIONS EVERY SINGLE SECOND**
