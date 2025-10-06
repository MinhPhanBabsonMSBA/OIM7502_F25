import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb # optional to set plot theme
sb.set_theme() # optional to set plot theme
import yfinance as yf

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())

class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()


    def get_data(self):
        """method that downloads data and stores in a DataFrame
           uncomment the code below wich should be the final two lines 
           of your method"""
        
        data = yf.download(self.symbol, start=self.start, end=self.end)
        # store in pd.DataFrame
        data = pd.DataFrame(data)
        # call calc_returns method to add change and return columns
        self.calc_returns(data)
        return data
        pass

    
    def calc_returns(self, df):
        """method that adds change and return columns to data"""
        df['Change'] = df['Close'].diff()
        df['LogReturn'] = np.log(df['Close']).diff().round(4)

        df.dropna(inplace=True)

        pass

    
    def plot_return_dist(self):
        """method that plots instantaneous returns as histogram"""
        plot = sb.histplot(self.data['LogReturn'], bins=50, kde=True)
        plt.title(f'{self.symbol} Return Distribution')
        plt.xlabel('LogReturn')
        plt.ylabel('Frequency')
        plt.show()
        pass


    def plot_performance(self):
        """method that plots stock object performance as percent """
        initial_price = self.data['Close'].iloc[0]
        performance = (self.data['Close'] - initial_price) / initial_price * 100
        plt.figure(figsize=(10, 6))
        plt.plot(self.data.index, performance, label=self.symbol)
        plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter())
        plt.title(f'{self.symbol} Performance Over Time')
        plt.xlabel('Date')
        plt.ylabel('Performance %')
        plt.legend()
        plt.show()
        pass                  



def main():
    # uncomment (remove pass) code below to test
    stock_symbol = 'AAPL'  # Example: Apple Inc. ticker symbol
    test = Stock(symbol=stock_symbol) # optionally test custom data range
    print(test.data)
    test.plot_performance()
    test.plot_return_dist()
if __name__ == '__main__':
    main() 