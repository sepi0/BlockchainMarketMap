from bs4 import BeautifulSoup
import requests
import re


class DataCollection(object):

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        self.data = self.soup.findAll("div", {"class": ""})
        self.table = []
        self.dates_data = []
        self.ohlcvm_data = []
        self.open = []
        self.high = []
        self.low = []
        self.close = []
        self.volume = []
        self.market_cap = []

    #
    def distribute_data(self):
        for item in self.data:
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
        for index in range(len(self.dates_data)):
            self.table.append({"Date": self.dates_data[index],
                               "Open": self.open[index],
                               "High": self.high[index],
                               "Low": self.low[index],
                               "Close": self.close[index],
                               "Volume": self.volume[index],
                               "MarketCap": self.market_cap[index]})

    def print_dictionary(self):
        for item in self.table:
            print(item)


if __name__ == '__main__':
    # tezos = DataCollection("https://coinmarketcap.com/currencies/tezos/historical-data/?start=20130429&end=20200301")
    # tezos.distribute_data()
    # tezos.generate_dictionary()
    # tezos.print_dictionary()

    bitcoin = DataCollection("https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130429&end=20200301")
    bitcoin.distribute_data()
    bitcoin.generate_dictionary()
    bitcoin.print_dictionary()
