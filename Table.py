from DataCollection import DataCollection
import pandas as pd


class Table(DataCollection):

    def __init__(self, name, url, element, attribute, value):
        super().__init__(name, url, element, attribute, value)

    def make_dataframe(self):
        self.generate_lists()
        self.generate_dictionary()
        # self.print_dictionary()
        df = pd.DataFrame.from_dict(self.full_data)
        print(df)
        df.to_excel('/home/sepio/{}.xlsx'.format(self.name))


if __name__ == '__main__':
    table = Table('Tezos',
                  'https://coinmarketcap.com/currencies/tezos/historical-data/?start=20130429&end=20200301',
                  "div",
                  "class",
                  "")
    table.make_dataframe()
