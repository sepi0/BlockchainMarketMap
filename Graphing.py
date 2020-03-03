from Table import Table
import plotly.graph_objects as go
import pandas as pd


class Graphing(Table):

    def __init__(self, name, url, element, attribute, value, filepath):
        super().__init__(name, url, element, attribute, value)
        self.filepath = filepath

    def candlestick_graph(self):
        # self.make_dataframe()
        df = pd.read_csv(self.filepath)
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                             open=df['Open'],
                                             high=df['High'],
                                             low=df['Low'],
                                             close=df['Close'])])
        fig.layout.update(xaxis_rangeslider_visible=False)
        fig.show()

if __name__ == '__main__':
    graph = Graphing('Tezos',
                      'https://coinmarketcap.com/currencies/tezos/historical-data/?start=20130429&end=20200301',
                      "div",
                      "class",
                      "", './Tezos.csv')
    graph.make_dataframe()
    graph.candlestick_graph()
