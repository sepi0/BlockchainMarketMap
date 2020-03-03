from bs4 import BeautifulSoup
import requests
import re
from timeit import default_timer as timer


class DataCollection(object):

    def __init__(self, name, url):
        self.url = url
        self.name = name
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.gather_data = self.soup.findAll("div", {"class": ""})
        self.full_data = []
        self.dates_data = []
        self.ohlcvm_data = []
        self.open = []
        self.high = []
        self.low = []
        self.close = []
        self.volume = []
        self.market_cap = []

    def __len__(self):
        return len(self.full_data)

    def __repr__(self):
        return '(Name: {!r}, Data: {!r})'.format(self.name, self.full_data)

    def __str__(self):
        return self.print_dictionary()

    def generate_lists(self):
        for item in self.gather_data:
            value = item.text
            if not re.search('[a-zA-Z!@#$%^&*]', value):
                self.ohlcvm_data.append(value)
            if len(item.text) == 12 and re.search(r'\d', item.text):
                self.dates_data.append(item.text)
        self.ohlcvm_data.pop(0)
        self.open = self.ohlcvm_data[0::6]
        self.high = self.ohlcvm_data[1::6]
        self.low = self.ohlcvm_data[2::6]
        self.close = self.ohlcvm_data[3::6]
        self.volume = self.ohlcvm_data[4::6]
        self.market_cap = self.ohlcvm_data[5::6]

    def generate_dictionary(self):
        self.ohlcvm_data.pop(0)
        for index in range(len(self.dates_data)):
            self.full_data.append({
                                "Date": self.dates_data[index],
                                "Open": self.open[index],
                                "High": self.high[index],
                                "Low": self.low[index],
                                "Close": self.close[index],
                                "Volume": self.volume[index],
                                "MarketCap": self.market_cap[index]})

    def print_dictionary(self):
        for item in self.full_data:
            print(item)


if __name__ == '__main__':
    tezos = DataCollection('Tezos', 'https://coinmarketcap.com/currencies/tezos/historical-data/?start=20130429&end=20200301')
    tezos.generate_lists()
    tezos.generate_dictionary()
