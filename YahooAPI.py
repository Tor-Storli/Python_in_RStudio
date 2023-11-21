import requests
import json
import datetime as dt_module

class YahooAPI:
        def __init__(self, symbol, date_range='1d', interval='1d'):
            self.symbol = symbol
            self.date_range = date_range
            self.interval = interval
            self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}

        def get_data_from_web_api(self):
            base_url = "https://query1.finance.yahoo.com/v8/finance/chart/"
            query_url = f"{self.symbol}?region=US&lang=en-US&includePrePost=false&interval={self.interval}&range={self.date_range}&corsDomain=finance.yahoo.com&.tsrc=finance"
            url = base_url + query_url
            print(url)
            response = requests.get(url, headers=self.headers)
            print("response status code:", response.status_code)
            return response.text

        def convert_timestamps(self, timestamps):
            return [dt_module.datetime.fromtimestamp(ts) for ts in timestamps]

        def parse_stock_data(self, json_data):
            data = json.loads(json_data)
            meta = data['chart']['result'][0]['meta']
            indicators = data['chart']['result'][0]['indicators']
            timestamps = self.convert_timestamps(data['chart']['result'][0]['timestamp'])

            # print(data)
            stock_data = {
                'timestamps': timestamps,
                'open': indicators['quote'][0]['open'],
                'high': indicators['quote'][0]['high'],
                'low': indicators['quote'][0]['low'],
                'close': indicators['quote'][0]['close'],
                'volume': indicators['quote'][0]['volume'],
                'adjclose': indicators['adjclose'][0]['adjclose']
            }

            return stock_data

        def get_stock_data(self):
            json_data = self.get_data_from_web_api()
            stock_data = self.parse_stock_data(json_data)
            return stock_data
            #return pd.DataFrame.from_dict(stock_data)
